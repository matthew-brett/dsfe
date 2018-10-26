""" Script to rebuild notebooks according to timestamps

* Search for .Rmd files in notebook directory;
* Is .Rmd later than corresponding .ipynb?
* If yes, write .Rmd, and execute .ipynb
* Is .ipynb later than corresponding _chapter?
* If yes, remove chapter.
* Do any chapters lack corresponding .ipynb files?
* If yes, remove chapter.
* Have we removed any chapters?
* If yes, build textbook
"""

import os
import sys
from os.path import (abspath, join as pjoin, splitext, sep as fsep,
                     getmtime, isfile, dirname, isdir)
from subprocess import check_call


def searchfor(path, extensions):
    """ Search `path` recursively for files with given `extensions`
    """
    if not isdir(path):
        return
    for entry in os.scandir(path):
        if entry.name.startswith('.'):
            continue
        if entry.is_dir(follow_symlinks=False):
            yield from searchfor(entry.path, extensions)
            continue
        for extension in extensions:
            if entry.name.endswith(extension):
                yield entry.path
                break


def debased(path, paths):
    """ Remove `path` prefix from iterable path names in `path`
    """
    deed = []
    path = path + fsep if not path.endswith(fsep) else path
    n = len(path)
    for p in paths:
        if p.startswith(path):
            p = p[n:]
        deed.append(p)
    return deed


def e_later(built, source):
    """ Return True if `built` exists, is later than `source`, False otherwise
    """
    if not isfile(built):
        return False
    return getmtime(built) > getmtime(source)


def same_e_later(built, source):
    """ Return True if `built` exists and is same time or later than `source`
    """
    if not isfile(built):
        return False
    return getmtime(built) >= getmtime(source)


class Build:

    nb_txt_ext = '.Rmd'
    source_exts = ('.ipynb', nb_txt_ext, '.md')
    built_exts = ('.ipynb', '.md')

    def __init__(self, site_root):
        self._set_paths(site_root)
        self.tb_files, self.nb_files = self._find_page_versions()
        self.bases = self._get_bases()

    def _set_paths(self, site_root):
        site_root = abspath(site_root)
        self.site_root = site_root
        self.site_textbook = pjoin(site_root, '_data', 'textbook.yml')
        self.config_file = pjoin(site_root, '_config.yml')
        self.template_path = pjoin(site_root, 'assets', 'templates',
                                   'jekyllmd.tpl')
        self.textbook_folder_name = '_chapters'
        self.notebooks_folder_name = 'notebooks'
        self.textbook_folder = pjoin(site_root, self.textbook_folder_name)
        self.notebooks_folder = pjoin(site_root, self.notebooks_folder_name)
        self.images_folder = pjoin(site_root, 'images')
        self.markdown_file = pjoin(site_root, 'SUMMARY.md')

    def _find_page_versions(self):
        """ Find notebook text, ipynb, chapter (.md) versions of notebooks

        Return found files in notebooks and chapters directories
        """
        return (
            list(searchfor(self.textbook_folder, self.built_exts)),
            list(searchfor(self.notebooks_folder, self.source_exts))
        )

    def _get_bases(self):
        """ Unique sub-path/basenames in notebook textbook directories
        """
        return sorted(set(splitext(p)[0] for p in (
            debased(self.textbook_folder, self.tb_files) +
            debased(self.notebooks_folder, self.nb_files))))

    def _delete_built(self, base, exts):
        tbb = pjoin(self.textbook_folder, base)
        for ext in exts:
            target = tbb + ext
            if isfile(target):
                os.unlink(target)

    def process_pages(self):
        rebuild = False
        for base in self.bases:
            nbb = pjoin(self.notebooks_folder, base)
            if nbb + '.md' in self.nb_files:
                rebuild = self.process_md(base) or rebuild
            elif nbb + self.nb_txt_ext in self.nb_files:
                rebuild = self.process_nb_txt(base) or rebuild
            elif nbb + '.ipynb' in self.nb_files:
                rebuild = self.process_ipynb(base) or rebuild
            else:
                # Now we must have chapters with deleted source.
                self._delete_built(base, self.built_exts)
        return rebuild

    def process_md(self, base):
        return self._process_in_ext(base, '.md', ('.md',))

    def _process_in_ext(self, base, in_ext, out_exts):
        tbb = pjoin(self.textbook_folder, base)
        nbb = pjoin(self.notebooks_folder, base)
        to_delete = list(self.built_exts)
        build_ok = all(same_e_later(tbb + out_ext, nbb + in_ext)
                       for out_ext in out_exts)
        if build_ok:
            to_delete = [ext for ext in self.built_exts
                         if ext not in out_exts]
        else:
            print('Rebuilding', tbb)
        self._delete_built(base, to_delete)
        return not build_ok

    def process_ipynb(self, base):
        return self._process_in_ext(base, '.ipynb', ('.md',))

    def process_nb_txt(self, base):
        nbb = pjoin(self.notebooks_folder, base)
        nb_src = nbb + self.nb_txt_ext
        nb_built = nbb + '.ipynb'
        build_ok = same_e_later(nb_built, nb_src)
        if build_ok:  # Defer to notebook check
            return self.process_ipynb(base)
        # Rebuild .ipynb
        check_call(['jupytext', '--to', 'notebook', nb_src])
        # Run .ipynb
        check_call(['jupyter', 'nbconvert', '--inplace',
                    '--ExecutePreprocessor.kernel_name=python3',
                    '--to', 'notebook', '--execute', nb_built])
        self._delete_built(base, self.built_exts)
        return True


def main():
    here = abspath(dirname(__file__))
    site_root = sys.argv[1] if len(sys.argv) > 1 else pjoin(here, '..')
    build = Build(site_root)
    rebuild = build.process_pages()
    if rebuild:
        print("Regenerating textbook")
        check_call(['python', pjoin(here, 'generate_textbook.py'),
                    '--site_root', site_root])
    else:
        print("Nothing to rebuild")


if __name__ == '__main__':
    main()
