---
interact_link: notebooks/01/3/Plotting_the_Classics.ipynb
title: '1.3 Plotting the Classics'
permalink: 'chapters/01/3/Plotting_the_Classics'
previouschapter:
  url: chapters/01/2/why-data-science
  title: '1.2 Why Data Science?'
nextchapter:
  url: chapters/01/3/1/Literary_Characters
  title: '1.3.1 Literary Characters'
redirect_from:
  - 'chapters/01/3/plotting-the-classics'
---

In this example, we will explore statistics for: *Alice's Adventures in
Wonderland* by Lewis Carroll.  The text of any book can be read by a computer
at great speed.  Books published before 1923 are currently in the *public
domain*, meaning that everyone has the right to copy or use the text in any
way. [Project Gutenberg](http://www.gutenberg.org/) is a website that
publishes public domain books online. Using Python, we can load the text of
these books directly from the web.

This example is meant to illustrate some of the broad themes of this text.
Don't worry if the details of the program don't yet make sense. Instead, focus
on interpreting the images generated below. Later sections of the text will
describe most of the features of the Python programming language used below.

First, we read the text of of the book into the memory of the computer.



{:.input_area}
```python
# Get the text for Alice in Wonderland
alice_url = 'https://www.gutenberg.org/files/11/11-0.txt'
alice_text = read_url(alice_url)
```


On the last line, Python gets the text of the book (`read_url(alice_url)`) and
gives it a name (`alice_text`). In Python, a name cannot contain any spaces,
and so we will often use an underscore `_` to stand in for a space. The `=` in
gives a name (on the left) to the result of some computation
described on the right.

A *uniform resource locator* or *URL* is an address on the Internet for some
content; in this case, the text of a book. The `#` symbol starts a comment,
which is ignored by the computer but helpful for people reading the code.

Now we have the text attached to the name `alice_text`, we can ask Python to
show us how the text starts:



{:.input_area}
```python
# Show the first 500 characters of the text
print(alice_text[:500])
```


You might want to check this is the same as the text you see by opening the
URL in your browser:
[https://www.gutenberg.org/files/11/11-0.txt](https://www.gutenberg.org/files/11/11-0.txt).

Now we have the text in memory, we can start to analyze it.  First we break
the text into chapters.  Don't worry about the details of the code, we will
cover these in the rest of the course.



{:.input_area}
```python
# Break the text into Chapters
alice_chapters = alice_text.split('CHAPTER ')
# Drop the first "Chapter" - it's the Project Gutenberg header
alice_chapters = alice_chapters[1:]
```


We can show the first half-line or so for each chapter, by putting the
chapters into a *table*.  You will see these tables or *data frames* many
times during this course.



{:.input_area}
```python
# Show the first few words of each chapter in a table.
pd.DataFrame(alice_chapters, columns=['Chapters'])
```

