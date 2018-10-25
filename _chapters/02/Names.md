---
interact_link: notebooks/02/Names.ipynb
title: '2.4 Names'
permalink: 'chapters/02/Names'
previouschapter:
  url: chapters/02/Expressions
  title: '2.3 Expressions'
nextchapter:
  url: chapters/02/Calls
  title: '2.5 Call expressions'
redirect_from:
  - 'chapters/02/names'
---

We have already seen [expressions](Expressions).

Python gives names to values in Python using an *assignment* statement. In an
assignment, a name is followed by `=`, which is followed by any expression.
The value of the expression to the right of `=` is *assigned* to the name.
Once a name has a value assigned to it, the value will be substituted for that
name in future expressions.



{:.input_area}
```python
a = 10
b = 20
a + b
```





{:.output_data_text}
```
30
```



A previously assigned name can be used in the expression to the right of `=`.



{:.input_area}
```python
quarter = 1/4
half = 2 * quarter
half
```





{:.output_data_text}
```
0.5
```



However, only the current value of an expression is assigned to a name. If
that value changes later, names that were defined in terms of that value will
not change automatically.



{:.input_area}
```python
quarter = 4
half
```





{:.output_data_text}
```
0.5
```



Names must start with a letter, but can contain both letters and numbers. A
name cannot contain a space; instead, it is common to use an underscore
character `_` to replace each space. Names are only as useful as you make
them; it's up to the programmer to choose names that are easy to interpret.
Typically, more meaningful names can be invented than `a` and `b`. For
example, let's say you were calculating the 20% Value Added Tax for a
restaurant bill, as well as 15% tip, on top of that.  The following names
clarify the meaning of the various quantities involved.



{:.input_area}
```python
meal_price = 25
vat_rate = 0.2
vat = meal_price * vat_rate
meal_price_with_vat = meal_price + vat
meal_price_with_vat
```





{:.output_data_text}
```
30.0
```





{:.input_area}
```python
tip_rate = 0.15
tip = meal_price_with_vat * tip_rate
meal_price_total = meal_price_with_vat + tip
meal_price_total
```





{:.output_data_text}
```
34.5
```



{% data8page Names %}
