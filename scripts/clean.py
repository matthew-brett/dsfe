import shutil as sh
from os.path import abspath, dirname, join as pjoin
from glob import glob

path_root = pjoin(dirname(abspath(__file__)), '..')

paths = [pjoin(path_root, 'images', 'chapters'),
         pjoin(path_root, '_site'),
         pjoin(path_root, '_data', 'textbook.yml')]
# Clean directories and files, but not .gitignore, in _chapters
paths += glob(pjoin(path_root, '_chapters', '*'))
for path in paths:
    print('Removing {}...'.format(path))
    sh.rmtree(path, ignore_errors=True)

print('Done!')
