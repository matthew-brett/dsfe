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


{:.output_stream}
```
﻿Project Gutenberg’s Alice’s Adventures in Wonderland, by Lewis Carroll

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: Alice’s Adventures in Wonderland

Author: Lewis Carroll

Posting Date: June 25, 2008 [EBook #11]
Release Date: March, 1994
Last Updated: October 6, 2016


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





<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chapters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>I. Down the Rabbit-Hole\r\n\r\nAlice was begin...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>II. The Pool of Tears\r\n\r\n‘Curiouser and cu...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>III. A Caucus-Race and a Long Tale\r\n\r\nThey...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>IV. The Rabbit Sends in a Little Bill\r\n\r\nI...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>V. Advice from a Caterpillar\r\n\r\nThe Caterp...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>VI. Pig and Pepper\r\n\r\nFor a minute or two ...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>VII. A Mad Tea-Party\r\n\r\nThere was a table ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>VIII. The Queen’s Croquet-Ground\r\n\r\nA larg...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>IX. The Mock Turtle’s Story\r\n\r\n‘You can’t ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>X. The Lobster Quadrille\r\n\r\nThe Mock Turtl...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>XI. Who Stole the Tarts?\r\n\r\nThe King and Q...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>XII. Alice’s Evidence\r\n\r\n\r\n‘Here!’ cried...</td>
    </tr>
  </tbody>
</table>
</div>
</div>


