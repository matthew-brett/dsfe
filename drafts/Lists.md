
# Lists
A list is a sequence of elements. The elements of a given list can have non-identical types. Square brackets are used to define a list, elements are accessed by indexing and slicing is available to generate sub-lists.


```python
my_mixed_list = [1.0, 5, 'today', 'tomorrow']
my_mixed_list
```




    [1.0, 5, 'today', 'tomorrow']



Slicing from **a** to **b**  `my_list[a:b]`, where **a** is included and **b** is not, eg **[a,b)**.


```python
my_mixed_list[1:3]
```




    [5, 'today']



Both **a** and **b** are optional. Try leaving **a**, **b** or both out and see what happens.


```python
my_mixed_list[2:]
```




    ['today', 'tomorrow']



Elements of lists can be arbitrary objects. Thus, `a = [2, [3, 4]]` is a valid list where the second element happens to be a list `([3, 4])`. Elements of lists can be modified individually.


```python
my_mixed_list[0] = 27
my_mixed_list
```




    [27, 5, 'today', 'tomorrow']



An empty list is defined as `a = []`. Lists have a number of methods they can invoke. Typing a list name followed by a full stop and then pressing *alt+tab* will bring up the names of methods that are available. A few examples are given below.




```python
a = ['1', 7, 7]
print('a: ', a)

a.append(8)
print('a.append(8) -> ', a)

print('a.index(7) -> ', a.index(7))

print('a.count(7) -> ', a.count(7))

a.remove(7)
print('a.remove(7) -> ', a)
```

    a:  ['1', 7, 7]
    a.append(8) ->  ['1', 7, 7, 8]
    a.index(7) ->  1
    a.count(7) ->  2
    a.remove(7) ->  ['1', 7, 8]


For convenience, `*` and `+` can be used with lists in an intuitive way:


```python
['1', 2]*3 + [4, 5]
```




    ['1', 2, '1', 2, '1', 2, 4, 5]


