```python
"""This is just for you so that you can see where the numbers are coming from.
It should be downloaded with the jupyter notebook, separately each file."""
np.random.seed(12345)

cars = np.random.randint(500,8000,size=500)
np.save('./cars.npy',cars)

value = np.random.uniform(size=500)
np.save('./value.npy',value)
```

# Assignment 5

Dan a university student wants to buy a car. He knows the price of each he is
considering and he assigned a value per pound ratio to each of the cars (based
on horsepower, consumption etc.). He saved this data in two arrays (clearly, why
wouldn't he?), where the order of the cars was the same. Obviously Dan doesn't
want a slow car, he wants the car to have at least $100$ horsepower, which start
from $1500$ pounds. So Dan did the following:

```python
# Import numpy
import numpy as np
```

First he loaded the arrays he created earlier, in the variable called cars and
value using a numpy function
[np.load()](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.load.html).

```python
cars = np.load('./cars.npy')
value_per_pounds = np.load('./value.npy')
```

Now he choose from the array the cars, which cost more, than the lower bound he
set for himself.

```python
cool_cars = cars[cars>1500]
```

He did the same to get rid of the value/price ratios, which are not relevant at
this point.

```python
cool_cars_value = value_per_pounds[cars>1500]
```

He really wanted to optimise the quality of his car for the price, therefore he
multiplied each car price with its value/pounds ratio, so that he got a
numerical value how good was each car. He knew that numpy worked pointwise,
therefore if he multiplies the two arrays each car respective value would have
been displayed in the new array.

```python
price_value = cool_cars * cool_cars_value
```

Luckily numpy knows how to get the index of the maximum value of an array, using
the
[np.argmax()](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.argmax.html)
function.

```python
best_value_index = np.argmax(price_value)
```

Thereby he knew the price of he car he wants to buy.

```python
cool_cars[best_value_index]
```

Dan was really happy that he finally did all the analysis and he can buy his new
car. However he realised that, since university started he spent too much time
in the pub, so he cannot afford the cars over $5000$ pounds. He got really sad
and he lost his motivation to the the analysis again, could you help Dan to buy
his new car?

## Help poor Dan:
