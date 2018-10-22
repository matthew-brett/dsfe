---
layout: single
title: Assignment 2
permalink: /assignments/assignment_2
redirect_from: /assignment_2
---

# Second assignment

If you squint your eyes and look sideways, this exercise is a little like the
classic [Pride and Prejudice and
Zombies](https://en.wikipedia.org/wiki/Pride_and_Prejudice_and_Zombies).

## Getting ready

Go to the [Literary Characters][litchar] page. Click
on "Download notebook" to download the notebook to your computer.

[litchar]: ../chapters/01/Literary_Characters
[anotherchar]: ../chapters/01/Another_Kind_Of_Character

I suggest you download to your `Desktop` folder.

Start the Jupyter Notebook (on Windows, press the Windows key and type
Jupyter Notebook).

You will now see a list of files and directories.  Click on "Desktop", and
select `Literary_Characters.ipynb`.  You should see a version of the notebook
that you saw on the [Literary Characters][litchar] page.

Click on the top cell of the notebook, and press shift at the same time as
Enter (or Return).  Keep doing that until you have gone through every cell.
It should run the same way as it did in class, but this time, on your own
computer.

## The exercise

Now see if you can read in the novel
[Dracula](https://en.wikipedia.org/wiki/Dracula) by Bram Stoker.  You can find
the full text of this book at <http://www.gutenberg.org/ebooks/345.txt.utf-8>.

### Rename the notebook

Go to the *File* menu, chose *Rename* and type in `look_at_dracula`.

### Change the URL to point to Bram Stoker's Dracula

In the notebook, replace this text:

```{python}
book_url = 'http://www.gutenberg.org/ebooks/42671.txt.utf-8'
```

with:

```{python}
book_url = 'http://www.gutenberg.org/ebooks/345.txt.utf-8'
```

Type shift with Enter to run the cell.  This will read in the text of
"Dracula" instead of "Pride and Prejudice".

### Change the character names to look for

We are going to look for these character names:

* Count (for Count Dracula),
* Harker (for Jonathan Harker, the hero),
* Mina (for Mina Murray, Harker's fiancé),
* Seward (for John Seward, Harker's friend),
* Helsing (for Abraham Van Helsing, Seward's teacher, and all-round expert),
* Quincey (for Quincey Morris, an American cowboy and explorer).

I know, only the female and the American characters have first names, I can
only apologize on behalf of Mr Stoker.  And Jane Austen, actually.  But hey.

Now look for the cell starting with:

```{python}
# Count how many times the characters appear in each chapter.
```

Replace `'Elizabeth'` with `'Count'`, so the first few lines of the cell look
like this:

```{python}
# Count how many times the characters appear in each chapter.
counts = pd.DataFrame.from_dict({
        'Count': np.char.count(alice_chapters, 'Count'),
```

Notice I replaced `'Elizabeth'` twice, once at the beginning and once at the
end of the line.

Now continue replacing:

* `'Darcy'` with `'Harker'`
* `'Lydia'` with `'Mina'`
* `'Wickham'` with `'Seward'`
* `'Bingley'` with `'Helsing'`
* `'Jane'` with `'Quincy'`

Try running the cell with shift-Enter.

If you get an error, look very carefully at the code - like all programming
languages, Python is very fussy about little things like commas and brackets.
Check [the original][litchar] to see if you can see the difference between
your current code and the original code cell.  Get someone else to have a
look, if you get stuck, you will be surprised how much difference it makes.

When you succeed in running the cell, have a look at the graph.

In roughly what chapter does the Count (Dracula) start to have a big role?
How about Van Helsing?

### Is there something funny about the chapters?

You may notice that all the characters seem to start rather late in the
chapter sequence.  Investigate to see why this is.  You may want to look at
the chapter lengths, using the code in [Another Kind of
Character][anotherchar], and by looking at the original text at
<http://www.gutenberg.org/ebooks/345.txt.utf-8>.  If you can, put an
explanation with some code at the end of the notebook to say what you think is
going on.
