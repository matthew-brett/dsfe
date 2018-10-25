---
interact_link: notebooks/01/Literary_Characters.ipynb
title: '1.3.1 Literary Characters'
permalink: 'chapters/01/Literary_Characters'
previouschapter:
  url: chapters/01/Plotting_the_Classics
  title: '1.3 Plotting the Classics'
nextchapter:
  url: chapters/01/Another_Kind_Of_Character
  title: '1.3.2 Another Kind of Character'
redirect_from:
  - 'chapters/01/literary-characters'
---

[Pride and Prejudice](https://en.wikipedia.org/wiki/Pride_and_Prejudice) is
the story of five sisters: Jane, Elizabeth, Mary, Kitty and Lydia, and their
journey through the social life of the mid-17th century.  You may remember
that Elizabeth ends up marrying the dashing and aloof Mr Darcy, but along the
way, the feckless Lydia runs off with the equally feckless Mr Wickham, and the
slightly useless Mr Bingley wants to marry Jane, the most beautiful of the
sisters.

We can see when these characters appear in the book, by counting how many
times their names are mentioned in each chapter.



{:.input_area}
```python
# Count how many times the characters appear in each chapter.
counts = pd.DataFrame.from_dict({
        'Elizabeth': np.char.count(book_chapters, 'Elizabeth'),
        'Darcy': np.char.count(book_chapters, 'Darcy'),
        'Lydia': np.char.count(book_chapters, 'Lydia'),
        'Wickham': np.char.count(book_chapters, 'Wickham'),
        'Bingley': np.char.count(book_chapters, 'Bingley'),
        'Jane': np.char.count(book_chapters, 'Jane')},
    )

# The cumulative counts:
# how many times in Chapter 1, how many times in Chapters 1 and 2, and so on.
cum_counts = counts.cumsum()

# Add the chapter numbers
number_of_chapters = len(book_chapters)
cum_counts['Chapter'] = np.arange(number_of_chapters)

# Do the plot
cum_counts.plot(x='Chapter')
plt.title('Cumulative Number of Times Each Name Appears');
```



![png](../../images/chapters/01/Literary_Characters_1_0.png)


In the plot above, the horizontal axis shows chapter numbers and the vertical
axis shows how many times each character has been mentioned up to and
including that chapter.

Notice first that Elizabeth and Darcy are the main characters.  Around chapter
13 we see Wickham and Lydia spike up, as they run away together, and mentions
of Darcy flatten off, when goes to look for them.   Around chapter 50 we see
Jane and Bingley being mentioned at a very similar rate, as Bingley proposes,
and Jane accepts.

{% data8page Literary_Characters %}
