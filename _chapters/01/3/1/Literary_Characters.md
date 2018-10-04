---
interact_link: notebooks/01/3/1/Literary_Characters.ipynb
title: '1.3.1 Literary Characters'
permalink: 'chapters/01/3/1/Literary_Characters'
previouschapter:
  url: chapters/01/3/Plotting_the_Classics
  title: '1.3 Plotting the Classics'
nextchapter:
  url: chapters/01/3/2/Another_Kind_Of_Character
  title: '1.3.2 Another Kind of Character'
redirect_from:
  - 'chapters/01/3/1/literary-characters'
---

This page is largely derived from `Literary_Characters` of the UC Berkeley
course \- see the license file on the main website.

In *Alice's Adventures in Wonderland*, Alice follows a white rabbit down a
rabbit hole, and finds herself in Wonderland.  After various adventures, she
finds herself at a tea party with the March Hare and the Hatter.  Afterwards,
she wanders into the royal court of the playing cards, including the Queen and
King of Hearts.

We can see when these characters appear in the book, by counting how many
times their names are mentioned in each chapter.



{:.input_area}
```python
# Count how many times the characters appear in each chapter.
counts = pd.DataFrame.from_dict({
        'Rabbit': np.char.count(alice_chapters, 'Rabbit'),
        'Hatter': np.char.count(alice_chapters, 'Hatter'),
        'Hare': np.char.count(alice_chapters, 'Hare'),
        'Queen': np.char.count(alice_chapters, 'Queen'),
        'King': np.char.count(alice_chapters, 'King')},
    )

# The cumulative counts:
# how many times in Chapter 1, how many times in Chapters 1 and 2, and so on.
cum_counts = counts.cumsum()

# Add the chapter numbers
number_of_chapters = len(alice_chapters)
cum_counts['Chapter'] = np.arange(number_of_chapters)

# Do the plot
cum_counts.plot(x='Chapter')
plt.title('Cumulative Number of Times Each Name Appears');
```



![png](../../../../images/chapters/01/3/1/Literary_Characters_1_0.png)


In the plot above, the horizontal axis shows chapter numbers and the vertical
axis shows how many times each character has been mentioned up to and
including that chapter.

Notice that the Rabbit appears in chapter 1, is missing from chapters 5, 6,
and 7, but returns for chapter 8.  The March Hare and the Hatter appear
at the same time, in chapter 7, which must be the tea party.  Last, the King
and Queen appear, in the chapters about the cards.
