---
layout: single
title: Exercise 2
permalink: /exercise_2
---

# Making your own notebooks

This exercise is to get y'all ready for the [assignment](assignment_2).

## Getting ready

Go to the [Literary Characters][litchar] page. Click
on "Download notebook" to download the notebook to your computer.

[litchar]: chapters/01/Literary_Characters
[anotherchar]: chapters/02/Another_Kind_Of_Character

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

Now see if you can read in the novel [Alice in
Wonderland](https://en.wikipedia.org/wiki/Alice%27s_Adventures_in_Wonderland)
by Lewis Carroll.

You can find the full text of this book at
<https://www.gutenberg.org/files/11/11-0.txt>.


### Rename the notebook

Go to the *File* menu, chose *Rename* and type in `alice`.

### Change the URL to point to Alice in Wonderland

In the notebook, replace this text:

```{python}
book_url = 'http://www.gutenberg.org/ebooks/42671.txt.utf-8'
```

with:

```{python}
book_url = 'https://www.gutenberg.org/files/11/11-0.txt'
```

Type shift with Enter to run the cell.  This will read in the text of
"Alice" instead of "Pride and Prejudice".

### Change the character names to look for

In *Alice's Adventures in Wonderland*, Alice follows a white rabbit down a
rabbit hole, and finds herself in Wonderland.  After various adventures, she
finds herself at a tea party with the March Hare and the Hatter.  Afterwards,
she wanders into the royal court of the playing cards, including the Queen and
King of Hearts.

We are going to look for these character names:

* Rabbit
* Hatter
* Hare (for the March Hare)
* Queen (for the Queen of Hearts)
* King (for the King of Hearts)
* Cheshire (for the Cheshire Cat)

Now look for the cell starting with:

```{python}
# Count how many times the characters appear in each chapter.
```

Replace `'Elizabeth'` with `'Rabbit'`, so the first few lines of the cell look
like this:

```{python}
# Count how many times the characters appear in each chapter.
counts = pd.DataFrame.from_dict({
        'Rabbit': np.char.count(alice_chapters, 'Rabbit'),
```

Notice I replaced `'Elizabeth'` twice, once at the beginning and once at the
end of the line.

Now continue replacing:

* `'Darcy'` with `'Hatter'`
* `'Lydia'` with `'Hare'`
* `'Wickham'` with `'Queen'`
* `'Bingley'` with `'King'`
* `'Jane'` with `'Jack'`

Try running the cell with shift-Enter.

If you get an error, look very carefully at the code - like all programming
languages, Python is very fussy about little things like commas and brackets.
Check [the original][litchar] to see if you can see the difference between
your current code and the original code cell.

When you succeed in running the cell, have a look at the graph.  Does it show
you anything about what happens in the book?
