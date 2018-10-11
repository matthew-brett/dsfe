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


{:.output_stream}
```
﻿The Project Gutenberg eBook, Pride and Prejudice, by Jane Austen, Edited
by R. W. (Robert William) Chapman


This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org





Title: Pride and Prejudice


Author: Jane Austen

Editor: R. W. (Robert William) Chapman

Release Date: May 9, 2013 

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
      <td>I.\r\n\r\n\r\nIt is a truth universally acknow...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>II.\r\n\r\n\r\nMr. Bennet was among the earlie...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>III.\r\n\r\n\r\nNot all that Mrs. Bennet, howe...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>IV.\r\n\r\n\r\nWhen Jane and Elizabeth were al...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>V.\r\n\r\n\r\nWithin a short walk of Longbourn...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>VI.\r\n\r\n\r\nThe ladies of Longbourn soon wa...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>VII.\r\n\r\n\r\nMr. Bennet's property consiste...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>VIII.\r\n\r\n\r\nAt five o'clock the two ladie...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>IX.\r\n\r\n\r\nElizabeth passed the chief of t...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>X.\r\n\r\n\r\nThe day passed much as the day b...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>XI.\r\n\r\n\r\nWhen the ladies removed after d...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>XII.\r\n\r\n\r\nIn consequence of an agreement...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>XIII.\r\n\r\n\r\n"I hope, my dear," said Mr. B...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>XIV.\r\n\r\n\r\nDuring dinner, Mr. Bennet scar...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>XV.\r\n\r\n\r\nMr. Collins was not a sensible ...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>XVI.\r\n\r\n\r\nAs no objection was made to th...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>XVII.\r\n\r\n\r\nElizabeth related to Jane the...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>XVIII.\r\n\r\n\r\nTill Elizabeth entered the d...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>XIX.\r\n\r\n\r\nThe next day opened a new scen...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>XX.\r\n\r\n\r\nMr. Collins was not left long t...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>XXI.\r\n\r\n\r\nThe discussion of Mr. Collins'...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>XXII.\r\n\r\n\r\nThe Bennets were engaged to d...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>XXIII.\r\n\r\n\r\nElizabeth was sitting with h...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>I.\r\n\r\n\r\nMiss Bingley's letter arrived, a...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>II.\r\n\r\n\r\nAfter a week spent in professio...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>III.\r\n\r\n\r\nMrs. Gardiner's caution to Eli...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>IV.\r\n\r\n\r\nWith no greater events than the...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>V.\r\n\r\n\r\nEvery object in the next day's j...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>VI.\r\n\r\n\r\nMr. Collins's triumph in conseq...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>VII.\r\n\r\n\r\nSir William staid only a week ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>IX.\r\n\r\n\r\nElizabeth was sitting by hersel...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>X.\r\n\r\n\r\nMore than once did Elizabeth in ...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>XI.\r\n\r\n\r\nWhen they were gone, Elizabeth,...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>XII.\r\n\r\n\r\nElizabeth awoke the next morni...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>XIII.\r\n\r\n\r\nIf Elizabeth, when Mr. Darcy ...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>XIV.\r\n\r\n\r\nThe two gentlemen left Rosings...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>XV.\r\n\r\n\r\nOn Saturday morning Elizabeth a...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>XVI.\r\n\r\n\r\nIt was the second week in May,...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>XVII.\r\n\r\n\r\nElizabeth's impatience to acq...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>XVIII.\r\n\r\n\r\nThe first week of their retu...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>XIX.\r\n\r\n\r\nHad Elizabeth's opinion been a...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>I.\r\n\r\n\r\nElizabeth, as they drove along, ...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>II.\r\n\r\n\r\nElizabeth had settled it that M...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>III.\r\n\r\n\r\nConvinced as Elizabeth now was...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>IV.\r\n\r\n\r\nElizabeth had been a good deal ...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>V.\r\n\r\n\r\n"I have been thinking it over ag...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>VI.\r\n\r\n\r\nThe whole party were in hopes o...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>VII.\r\n\r\n\r\nTwo days after Mr. Bennet's re...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>VIII.\r\n\r\n\r\nMr. Bennet had very often wis...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>IX.\r\n\r\n\r\nTheir sister's wedding day arri...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>X.\r\n\r\n\r\nElizabeth had the satisfaction o...</td>
    </tr>
    <tr>
      <th>52</th>
      <td>XI.\r\n\r\n\r\nMr. Wickham was so perfectly sa...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>XII.\r\n\r\n\r\nAs soon as they were gone, Eli...</td>
    </tr>
    <tr>
      <th>54</th>
      <td>XIII.\r\n\r\n\r\nA few days after this visit, ...</td>
    </tr>
    <tr>
      <th>55</th>
      <td>XIV.\r\n\r\n\r\nOne morning, about a week afte...</td>
    </tr>
    <tr>
      <th>56</th>
      <td>XV.\r\n\r\n\r\nThe discomposure of spirits, wh...</td>
    </tr>
    <tr>
      <th>57</th>
      <td>XVI.\r\n\r\n\r\nInstead of receiving any such ...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>XVII.\r\n\r\n\r\n"My dear Lizzy, where can you...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>XVIII.\r\n\r\n\r\nElizabeth's spirits soon ris...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>XIX.\r\n\r\n\r\nHappy for all her maternal fee...</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 1 columns</p>
</div>
</div>



This is your first view of a data frame.  Ignore the first column for now - it
is just a row number.  The second column shows the first few characters of the
text in the chapter.   The text starts with the chapter number in Roman
numerals.  You might want to check the text from the link above to reassure
yourself that this comes from the text we downloaded.  Next you see some odd
characters with backslashes, such as `\r` and `\n`.  These are representations
of new lines, or paragraph marks.  Last you will see the beginning of the
first sentence of the chapter.
