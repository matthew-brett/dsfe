
# Lists
## C3PO
Imagine you had a robot that would do chores for you. All you have to do is provide it with a task and it will be done. And, of course, as any respectable robot, your robot communicates in python. 

So you start easy and give your robot just one task:


```python
task = "do the dishes"
```

But keeping track of when the robot finishes one task in order to manually type in the other one is almost as troublesome as doing everything yourself. Wouldn't it be amazing if you could create a *list* of tasks?


```python
tasks = ["do the dishes", "buy groceries", "eliminate all the sadness in the world", "vacuum floors"]
```

### Indexing
Great! Now you have created a [list](https://docs.python.org/3/tutorial/introduction.html#lists). Lists contain elements, separated by commas. They start and end with a square bracket.

In order to see a particular element of a list, one writes `my_list[index]`, where `my_list` is the name of your list and `index` is the index number of the element.

Try printing out the very first task from the `tasks` list.

Since you are very curious, you also try putting a negative number as `index`

As you may have guessed, negative indices count the elements of a list from rigt to left, with `-1` being the very last element. This means that for our list of four elements, positive indices are going from `0` to `3`, while negative indices go from `-1` to `-4`.


```python
tasks[0]
```




    'do the dishes'




```python
tasks[-4]
```




    'do the dishes'



What values will the following commans return?


```python
tasks[3]
```


```python
tasks[-3]
```

### Slicing
Okay, now you can now you can send your robot a whole list of tasks and if you really feel like it, you can look at that one by one. This way you can, for example, see what is the first task your robot is going to do today.

But what if you want more? Would it be maybe possible to view not one just element, not the whole gigantic list, but a few elements at a time? A smaller sub-list, part of the original list. One might even call it a *slice*.


```python
tasks[1:3]
```




    ['buy groceries', 'eliminate all the sadness in the world']



Slicing from **a** to **b**  `my_list[a:b]`, where **a** is included and **b** is not, eg **[a,b)**.

You can think of it this way: if you leave the first value out and just type `tasks[:2]` you are going to get first **two** elements. 


```python
tasks[:2]
```




    ['do the dishes', 'buy groceries']



While if you do the opposite, `tasks[2:]`, python will cut off the first **two** elements.


```python
tasks[2:]
```




    ['eliminate all the sadness in the world', 'vacuum floors']



So then `tasks[2:3]` is equivalent to, firstly, looking at first **three** elements of the list,


```python
short_list = tasks[:3]
short_list
```




    ['do the dishes', 'buy groceries', 'eliminate all the sadness in the world']



and then removing the first **two** from that:


```python
short_list[2:]
```




    ['eliminate all the sadness in the world']



### Changing
After a careful examination, you decide that maybe eliminating all the sadness in the world is a bit too hard of a task for your robot. Besides, then it won't have time to vacuum your floors, and we all know what's more important.

Lists are *mutable* objects. This means you can change their content with `my_list[index] = value`, where `value` is, you guessed it, your new value. 

Change our unrealistic task to something more doable, say, "cook dinner".

### Adding
It might also be a good idea to make sure your robot returns back to the charging station at the end of the day. You can add new elements at the end of the list by using `my_list.append(value)`.

Add "recharge" to the end of the list of tasks.
