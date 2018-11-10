# Assignment 6

Dan a university student wants to buy a car. He knows the price
of each he is
considering and he assigned a value per pound ratio to each of the
cars (based
on horsepower, consumption etc.). He typed this data in two arrays
(clearly, why
wouldn't he?), where the order of the cars was the same. Obviously
Dan doesn't
want a slow car, he wants the car to have at least $100$ horsepower,
which start
from $1500$ pounds. So Dan did the following:

```python
# Import numpy
import numpy as np
```

Use diligent Dan's typed data set:

```python
cars = np.array([5360,  558, 2749, 6549, 2814,  587,  501, 5800, 3670,
                 4549, 6980, 7622, 6242, 6674, 6159, 6924, 1457, 7808,
                 1585, 3591, 7534, 4274, 4751, 3182,  656, 1686, 2303,
                 2317, 4576, 1740])
value_per_pounds = np.array([0.67, 0.66, 0.48, 0.09, 0.27, 0.64, 0.55,
                             0.77, 0.24, 0.19, 0.19, 0.46, 0.03, 0.48,
                             0.61, 0.84, 0.23, 0.8 , 0.55, 0.81, 0.61,
                             0.3 , 0.87, 0.83, 0.97, 0.56, 0.15, 0.75,
                             0.57, 0.33])
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
numerical value how good was each car. He knew that numpy worked elementwise,
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

Thereby he knew the price of he car he wants to buy, hence identify it.

```python
cool_cars[best_value_index]
```

Dan was really happy that he finally did all the analysis and he can buy his new
car. However he realised that, since university started he spent too much time
in the pub, so he cannot afford the cars over $5000$ pounds. He got really sad
and he lost his motivation to the the analysis again, could you help Dan to buy
his new car?

## Help poor Dan:
