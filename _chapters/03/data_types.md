---
interact_link: notebooks/03/data_types.ipynb
title: '3. Data types'
permalink: 'chapters/03/data_types'
previouschapter:
  url: chapters/02/Calls
  title: '2.5 Call expressions'
nextchapter:
  url: chapters/03/Numbers
  title: '3.1 Numbers'
redirect_from:
  - 'chapters/03/data-types'
---

# Types of things

Every object in Python, has a type.

We can show what type of thing something is, by calling `type`, like this:



{:.input_area}
```python
type(1)
```





{:.output_data_text}
```
int
```





{:.input_area}
```python
type(1.0)
```





{:.output_data_text}
```
float
```





{:.input_area}
```python
a = 1
type(a)
```





{:.output_data_text}
```
int
```



If you get stuck in some code, it is often useful to check what types the objects are.

We will use multiple types when analyzing data.  We cover some of the common ones, in this chapter.
