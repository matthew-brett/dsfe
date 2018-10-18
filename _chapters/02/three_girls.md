---
interact_link: notebooks/02/three_girls.ipynb
title: '2.2 A simpler problem'
permalink: 'chapters/02/three_girls'
previouschapter:
  url: chapters/02/sampling_problem
  title: '2.1 A sampling problem'
nextchapter:
  url: chapters/02/Expressions
  title: '2.3 Expressions'
redirect_from:
  - 'chapters/02/three-girls'
---

# A simpler problem

Imagine a family with four children.

What is the probability that the family will have exactly three girls?

There are various ways to answer this question.  One way, is to use
*simulation*.

Simulation makes a *model* of the problem.  We use the model to generate
*simulated* data.  If the model is a good one, the simulated data should look
like the real data.

First we need to simulate a family of four children.

Then we need to count the number of girls.

We do this many many times, and see how often we get a count of 3.



{:.input_area}
```python
np.random.uniform()
```





{:.output_data_text}
```
0.485136637823122
```



As we will soon see, we are using a *call expression* here.  `np.random.uniform()` *calls* the function, and returns a random number, between 0 and 1.

It's inconvenient to have to run this cell many times.   We really need some machinery to make the computer do that for us.  We need *expressions*, *names*, *call expressions, *comparisons* and *arrays*.  We will deal with those next.
