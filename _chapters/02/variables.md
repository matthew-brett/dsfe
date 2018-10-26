---
interact_link: notebooks/02/variables.ipynb
title: '2.4 Variables'
permalink: 'chapters/02/variables'
previouschapter:
  url: chapters/02/Expressions
  title: '2.3 Expressions'
nextchapter:
  url: chapters/02/Names
  title: '2.5 Names'
redirect_from:
  - 'chapters/02/variables'
---

Variables are - things that vary.

You remember variables like $x$ and $y$ from mathematics.

In mathematics, we can use names, such as $x$ and $y$, to represent any value.

In the piece of mathematics below, we define $y$ given any value for $x$:

$$
y = 3x + 2
$$

When we have some value for $x$, we can get the corresponding value of $y$.

We give $x$ some value:

$$
x = 4
$$

We apply the rule above to give a value to $y$:

$$
y = 3 * x + 2 \\
= 3 * 4 + 2 \\
= 14
$$

"x" is a name that refers to a value.  We use the name to *represent* the
value.  In the expression above, $x$ represents the value 4.  Of course we
could give $x$ any value.

Variables in Python work in the same way.

Variables are *names* given to *values*.  We can use the name to refer to the
value in calculations.

For example, here I say that the *name* `x` refers to the *value* 4:



{:.input_area}
```python
x = 4
```


Now I can calculate a value, using that name:



{:.input_area}
```python
3 * x + 2
```





{:.output_data_text}
```
14
```



## Variables in expressions

This is an *expression*.  You have seen expressions with numbers, but here we
have an expression with numbers and a variable.  When Python sees the variable
name `x` in this expression, it *evaluates* `x`, and gets the value that it
refers to.  After Python has evaluated `x` to get 4, it ends up with this:



{:.input_area}
```python
3 * 4 + 2
```





{:.output_data_text}
```
14
```



I can also give a name to the *result* of this expression - such as `y`:



{:.input_area}
```python
y = 3 * x + 2
```




{:.input_area}
```python
y
```





{:.output_data_text}
```
14
```



If I change `x`, I change the result:



{:.input_area}
```python
x = 5
y = 3 * x + 2
y
```





{:.output_data_text}
```
17
```



Variables are essential in mathematics, to express general rules for
calculation.  For the same reason, variables are essential in Python.

In mathematics, we usually prefer variables with very short names - $x$ or $y$
or $p$.  This makes them easier to read on the page.

In Python, and other programming languages, we can use variables with longer
names, and we usually do, because we use so many variables.  Giving them
longer names helps us remember what the variables are for.

[Next](Names) we go into more detail about names and expressions.
