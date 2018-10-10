---
layout: single
title: Assignment 2
permalink: /assignment_2
---

# Second assignment

Go to the [Literary Characters](_chapters/01/3/1/Literary_Characters)
page. Click on "Interact" to load up the notebook in your browser.

When the notebook is open, click on the File menu, chose "Download as ..." and
select "Notebook (.ipynb)".  Save the file to your Desktop.

Start the Anaconda Navigator (on Windows, press the Windows key and type
Anaconda Navigator).  Click "Launch" for the Jupyter Notebook, to start the
notebook software on your own computer.

You will now see a list of files and directories.  Click on "Desktop", and
select `Literary_Characters.ipynb`.  You should see the same notebook as you
saw before, when you clicked "Interact".

Click on the top cell of the notebook, and press shift at the same time as
Enter (or Return).  Keep doing that until you have gone through every cell.
It should run the same way as it did in class, but this time, on your own
computer.

Now see if you can read in the novel "Dracula" by Bram Stoker.  You can find
the full text of this book at
<http://www.gutenberg.org/cache/epub/345/pg345.txt>

In the notebook, replace this text:

```{python}
alice_url = 'https://www.gutenberg.org/files/11/11-0.txt'
```

with:

```{python}
alice_url = 'http://www.gutenberg.org/cache/epub/345/pg345.txt'
```

Type shift with Enter to run the cell.  This will read in the text of
"Dracula" instead of "Alice's Adventures in Wonderland".

We are going to look for these character names:

* Count (for Count Dracula),
* Harker (for Jonathan Harker, the hero),
* Mina (for Mina Murray, Harker's fiancé),
* Seward (for John Seward, Harker's friend),
* Helsing (for Abraham Van Helsing, Seward's teacher, and all-round expert).

I know, only the female character has a first name, I can only apologize for
Mr Stoker.

Now

```{python}
# Count how many times the characters appear in each chapter.
```

Replace `'Rabbit'` with `'Count'`, so the first few lines of the cell look like
this:

```{python}
# Count how many times the characters appear in each chapter.
counts = pd.DataFrame.from_dict({
        'Count': np.char.count(alice_chapters, 'Count'),
```

Notice I replaced `'Rabbit'` twice, once at the beginning and once at the end
of the line.

Now continue replacing:

* `'Hatter'` with `'Harker'`
* `'Hare'` with `'Mina'`
* `'Queen'` with `'Seward'`
* `'King'` with `'Helsing'`

Try running the cell with shift-Enter.

In roughly what chapter does the Count (Dracula) start to have a big role?
How about Van Helsing?

Any problems, see the Canvas page for email and office hours.
