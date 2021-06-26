# Data science for everyone

This is tomogwen's fork of the README

Course materials and notes for the course Data Science for Everyone.

This textbook is based on the Berkeley Foundations of Data Science
course. The most recent version of the course is at [Computational and
Inferential Thinking](https://www.inferentialthinking.com).  The
repository for the textbook is [on
Github](https://github.com/data8/textbook).

Versions of the Berkeley course come from the last commit in that
repository that is licensed with a Creative Commons CC-BY-NC license
- `64b20f0`.  The following commit (`710ed4e`) relicensed the work
with a CC-BY-NC-ND license, forbidding derivative works.

## Machinery

The template for this website comes from
<https://github.com/choldgraf/textbooks-with-jupyter> - many thanks to
Chris Holdgraf for putting that together.

## Getting started for working on the repository

Say your Github username is `my-gh-user`.

Go to the repository page <https://github.com/matthew-brett/dsfe>.

Click on "Fork" button near top right, to make your own fork of the
repository, that will now be at `https://github.com/my-gh-user/dsfe`.

**Before you clone the repository**, make sure you are working in
a case-sensitive filesystem.  The default macOS filesystem is not
case-sensitive, see the section "Case-sensitive files on the Mac" near
the end, before you continue, and clone into this new filesystem.

Clone the main repo:

```
git clone https://github.com/matthew-brett/dsfe
```

Add a remote for your fork:

```
cd dsfe
git remote add my-gh-user https://github.com/my-gh-user/dsfe.git
git fetch my-gh-user
```

Get the submodules for the repository (you'll need these for the
build):

```
git submodule update --init
```

Start by making some branch to work on, linked to your fork.  Use
a name to match the kind of changes you are about to make, like
`rewrite-intro-pages`:

```
git branch rewrite-intro-pages
git checkout rewrite-intro-pages
```

Associate this branch with your fork:

```
git push my-gh-user rewrite-intro-pages -u
```

The `-u` flag above stores the association of this branch with your
fork, referenced by `my-gh-user`.

## Installing stuff for building / serving the repository files

If you use [Conda](https://conda.io/docs) then you might make a Conda
environment for working on the repo.  I don't, I use pip, and I make
a virtual environment.  You can do that like this:

```
python3 -m venv my-venv
source my-virtualenv/bin/activate
```

Or, if you have
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/)
(I do) then, you might prefer:

```
python3 -m venv $WORKON_HOME/my-venv
workon my-venv
```

Install the Python packages you need for building the site:

```
pip install -r build-requirements.txt
```

Install the site build / serve engine, [Jekyll](https://jekyllrb.com),
by following the [Jekyll install
instructions](https://jekyllrb.com/docs/installation).

Finish up with a final:

```
bundle install
```

Finally, check that you can run the local website server with:

```
make serve
```

Copy the URL that comes up, and paste into your browser's URL bar, to
check you get can load the local website copy.

## Configuring Jupyter to save / load in R Markdown

I'm using the excellent [Jupytext](https://github.com/mwouts/jupytext)
to make it easier to edit Jupyter Notebooks.  Jupytext automates
saving Notebook files as Markdown (and other formats), and loading
them from edited Markdown (and other formats).

You need to configure Jupyter to use it.  If you don't have a Jupyter
configuration, do:

```
jupyter notebook --generate-config
```

You should now have a file `~/.jupyter/jupyter_notebook_config.py`.
Append these lines:

```
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
c.ContentsManager.default_jupytext_formats = "ipynb,Rmd"
```

I also turned off autosave globally, by following the instructions [in
this stackoverflow answer](https://stackoverflow.com/a/45980165).
This stops autosave saving over any edits that I am making in the
Markdown source.

**Be careful** - if you are used to autosave in Jupyter, you can
easily lose work when you disable autosave.

```
mkdir -p ~/.jupyter/custom
```

Add the following line to `~/.jupyter/custom/custom.js`:

```
Jupyter.notebook.set_autosave_interval(0); // disable autosave
```

Finally, you may want to clone the original Berkeley textbook:

```
# Get out of dsfe tree
cd ..
git clone https://github.com/data-8/textbook
```

**Make sure you are using the last commit we can legally use, from the
Berkeley repository**:

```
cd textbook
# Checkout the last CC-BY-NC commit
git checkout 64b20f0
```

## Extra stuff

Consider installing [hub](https://github.com/github/hub) to make
interactions with Github easier, from the command line.

## Configuring build etc

You might want to check the instructions for configuring the build at
<https://github.com/choldgraf/textbooks-with-jupyter>.

## Workflow

### Developing

* `make serve` to run the local server serving `_site` directory.
* Attach browser to <http://localhost:4000/dsfe/> as suggested in
  output of `make serve`.
* Edit `.Rmd` and / or `.ipynb` files
* `make rebuild-notebooks` to rebuild `.ipynb` from more recent `.Rmd`
  files, and rebuild `.md` files from more recent `.ipynb` files.
* Review in browser

### Shipping

* Final check
* Ship with `make github`

## Case-sensitive filesystem on the Mac

The default file-systems for current Macs are Journalled HFS+, or
APFS, neither of which are case-sensitive by default.  This causes
problems with file-names for the built files - see
<https://github.com/choldgraf/jupyter-book/pull/27>.

You can check if you are on a case-sensitive file-system with:

```
mkdir tmp
touch tmp/abcd.txt
touch tmp/abcD.txt
ls tmp/ab*.txt
```

If you see only one file listed, you're on a case-insensitive
file-system, and this will cause problems for editing and uploading
the files in this repo.

### The easy way, with modern macOS

The easiest way to solve this, on a modern Mac, is to make a new
case-sensitive APFS volume.  Go to Disk Utility, click on a hard
drive, click on the `+` icon at the top left, under "Volume", and you
should get a GUI for "Add APFS volume to a container?".  Choose "APFS
(Case-sensitive)".  With all done, you should have a new volume, into which you can clone the repository.

### The hard way, with older macOS

If you do not have the option above, you can also make a new disk image file, and mount that.  In my hands, this started to get very slow, as the disk image got close to full.  Here are the instructions in case you want to give it a go:

* Make a *disk image* with a case-sensitive file-system on it.
* Mount the disk image
* Work inside the mounted disk image.

Clone this Gist:

```
git clone https://gist.github.com/faa9ccc0d7cb2936263f16192106a98a
```

Have a look at the `.plist` file inside, and follow the instructions
in the comments, to set this up.  When you have followed the
instructions, you should find that the system mounts the image
automatically when you log in.
