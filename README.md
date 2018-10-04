# Data science for everyone

Course materials and notes for the course Data Science for Everyone.

This textbook is based on the Berkeley Foundations of Data Science course.
The most recent version of the course is at [Computational and Inferential
Thinking](https://www.inferentialthinking.com).  The repository for the
textbook is [on Github](https://github.com/data8/textbook).

Versions of the Berkeley course come from the last commit in that repository
that is licensed with a Creative Commons CC-BY-NC license - `64b20f0`.  The
following commit (`710ed4e`) relicensed the work with a CC-BY-NC-ND license,
forbidding derivative works.

## Machinery

The template for this website comes from
https://github.com/choldgraf/textbooks-with-jupyter - many thanks to Chris
Holdgraf for putting that together.

To start working on the book, get into a `virtualenv` or similar, and:

```
pip install -r build-requirements.txt
```

You might want to check the instructions for configuring the build at
https://github.com/choldgraf/textbooks-with-jupyter.

I'm using the excellent [Jupytext](https://github.com/mwouts/jupytext) to make
my life easier, editing Jupyter Notebooks.  Specifically, I put these lines
into `~/.jupyter/jupyter_notebook_config.py`:

```
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
c.ContentsManager.default_jupytext_formats = "ipynb,Rmd"
```

I also turned off autosave globally, by following the instructions [in this
stackoverflow answer](https://stackoverflow.com/a/45980165).  It suggests
adding the following line to `~/.jupyter/custom/custom.js`:

```
Jupyter.notebook.set_autosave_interval(0); // disable autosave
```

At the moment, I'm editing and committing the resulting `.Rmd` and `.ipynb`
files, but a better workflow would be to build the `.ipynb` files
automatically.
