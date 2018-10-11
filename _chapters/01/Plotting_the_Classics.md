---
interact_link: notebooks/01/Plotting_the_Classics.ipynb
title: '1.3 Plotting the Classics'
permalink: 'chapters/01/Plotting_the_Classics'
previouschapter:
  url: chapters/01/2/why-data-science
  title: '1.2 Why Data Science?'
nextchapter:
  url: chapters/01/Literary_Characters
  title: '1.3.1 Literary Characters'
redirect_from:
  - 'chapters/01/plotting-the-classics'
---

This page is largely derived from `Plotting_the_Classics` of the UC Berkeley
course \- see the license file on the main website.

In this example, we will explore statistics for: *Pride and Prejudice*
by Jane Austen.  The text of any book can be read by a computer at great
speed.  Books published before 1923 are currently in the *public domain*,
meaning that everyone has the right to copy or use the text in any way.
[Project Gutenberg](http://www.gutenberg.org/) is a website that publishes
public domain books online. Using Python, we can load the text of these books
directly from the web.

This example is meant to illustrate some of the broad themes of this text.
Don't worry if the details of the program don't yet make sense. Instead, focus
on interpreting the images generated below. Later sections of the text will
describe most of the features of the Python programming language used below.

First, we read the text of of the book into the memory of the computer.



{:.input_area}
```python
# Get the text for Pride and Prejudice
book_url = 'http://www.gutenberg.org/ebooks/42671.txt.utf-8'
book_text = read_url(book_url)
```


On the last line, Python gets the text of the book (`read_url(book_url)`) and
gives it a name (`book_text`). In Python, a name cannot contain any spaces,
and so we will often use an underscore `_` to stand in for a space. The `=` in
gives a name (on the left) to the result of some computation
described on the right.

A *uniform resource locator* or *URL* is an address on the Internet for some
content; in this case, the text of a book. The `#` symbol starts a comment,
which is ignored by the computer but helpful for people reading the code.

Now we have the text attached to the name `book_text`, we can ask Python to
show us how the text starts:



{:.input_area}
```python
# Show the first 500 characters of the text
print(book_text[:500])
```


You might want to check this is the same as the text you see by opening the
URL in your browser: <http://www.gutenberg.org/ebooks/42671.txt.utf-8>

Now we have the text in memory, we can start to analyze it.  First we break
the text into chapters.  Don't worry about the details of the code, we will
cover these in the rest of the course.



{:.input_area}
```python
# Break the text into Chapters
book_chapters = book_text.split('CHAPTER ')
# Drop the first "Chapter" - it's the Project Gutenberg header
book_chapters = book_chapters[1:]
```


We can show the first half-line or so for each chapter, by putting the
chapters into a *table*.  You will see these tables or *data frames* many
times during this course.



{:.input_area}
```python
# Show the first few words of each chapter in a table.
pd.DataFrame(book_chapters, columns=['Chapters'])
```


This is your first view of a data frame.  Ignore the first column for now - it
is just a row number.  The second column shows the first few characters of the
text in the chapter.   The text starts with the chapter number in Roman
numerals.  You might want to check the text from the link above to reassure
yourself that this comes from the text we downloaded.  Next you see some odd
characters with backslashes, such as `\r` and `\n`.  These are representations
of new lines, or paragraph marks.  Last you will see the beginning of the
first sentence of the chapter.
