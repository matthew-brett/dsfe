
# Data Frames
We will start, as usual, by importing all the libraries we need.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Fancy plots
plt.style.use('fivethirtyeight')
```

Now we are going to need some data. Go ahead and download [iris.csv](https://matthew-brett.github.io/dsfe/data/iris.csv) and import it as a dataframe (save the file to the same directory from which you are running this notebook to make your life easier).


```python
iris = pd.read_csv('iris.csv')
```

At this moment we have no clue about what data are contained inside this dataframe. First thing we can do is simply print out the whole dataframe.


```python
iris
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.4</td>
      <td>3.9</td>
      <td>1.7</td>
      <td>0.4</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.6</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.3</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.0</td>
      <td>3.4</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.4</td>
      <td>2.9</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.4</td>
      <td>3.7</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4.8</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4.3</td>
      <td>3.0</td>
      <td>1.1</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>14</th>
      <td>5.8</td>
      <td>4.0</td>
      <td>1.2</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5.7</td>
      <td>4.4</td>
      <td>1.5</td>
      <td>0.4</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>16</th>
      <td>5.4</td>
      <td>3.9</td>
      <td>1.3</td>
      <td>0.4</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.3</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>18</th>
      <td>5.7</td>
      <td>3.8</td>
      <td>1.7</td>
      <td>0.3</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5.1</td>
      <td>3.8</td>
      <td>1.5</td>
      <td>0.3</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5.4</td>
      <td>3.4</td>
      <td>1.7</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>21</th>
      <td>5.1</td>
      <td>3.7</td>
      <td>1.5</td>
      <td>0.4</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>22</th>
      <td>4.6</td>
      <td>3.6</td>
      <td>1.0</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5.1</td>
      <td>3.3</td>
      <td>1.7</td>
      <td>0.5</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>24</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>25</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>26</th>
      <td>5.0</td>
      <td>3.4</td>
      <td>1.6</td>
      <td>0.4</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>27</th>
      <td>5.2</td>
      <td>3.5</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>28</th>
      <td>5.2</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>29</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>120</th>
      <td>6.9</td>
      <td>3.2</td>
      <td>5.7</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>121</th>
      <td>5.6</td>
      <td>2.8</td>
      <td>4.9</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>122</th>
      <td>7.7</td>
      <td>2.8</td>
      <td>6.7</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>123</th>
      <td>6.3</td>
      <td>2.7</td>
      <td>4.9</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>124</th>
      <td>6.7</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.1</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>125</th>
      <td>7.2</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>126</th>
      <td>6.2</td>
      <td>2.8</td>
      <td>4.8</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>127</th>
      <td>6.1</td>
      <td>3.0</td>
      <td>4.9</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>128</th>
      <td>6.4</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>2.1</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>129</th>
      <td>7.2</td>
      <td>3.0</td>
      <td>5.8</td>
      <td>1.6</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>130</th>
      <td>7.4</td>
      <td>2.8</td>
      <td>6.1</td>
      <td>1.9</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>131</th>
      <td>7.9</td>
      <td>3.8</td>
      <td>6.4</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>132</th>
      <td>6.4</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>2.2</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>133</th>
      <td>6.3</td>
      <td>2.8</td>
      <td>5.1</td>
      <td>1.5</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>134</th>
      <td>6.1</td>
      <td>2.6</td>
      <td>5.6</td>
      <td>1.4</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>135</th>
      <td>7.7</td>
      <td>3.0</td>
      <td>6.1</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>136</th>
      <td>6.3</td>
      <td>3.4</td>
      <td>5.6</td>
      <td>2.4</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>137</th>
      <td>6.4</td>
      <td>3.1</td>
      <td>5.5</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>138</th>
      <td>6.0</td>
      <td>3.0</td>
      <td>4.8</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>139</th>
      <td>6.9</td>
      <td>3.1</td>
      <td>5.4</td>
      <td>2.1</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>140</th>
      <td>6.7</td>
      <td>3.1</td>
      <td>5.6</td>
      <td>2.4</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>141</th>
      <td>6.9</td>
      <td>3.1</td>
      <td>5.1</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>142</th>
      <td>5.8</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.9</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>143</th>
      <td>6.8</td>
      <td>3.2</td>
      <td>5.9</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>144</th>
      <td>6.7</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.5</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 5 columns</p>
</div>



But more often than not we don't need to see ~60 entires to get the idea of what we are looking at. All we want is the column names and some examples to understand the format the data are in. For these purposes we can use `head` method of the data frame.


```python
iris.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



By default, `head()` displays first five entries, but we have the option to passs it a specific number of rows we want to see.


```python
iris.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.4</td>
      <td>3.9</td>
      <td>1.7</td>
      <td>0.4</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.6</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.3</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.0</td>
      <td>3.4</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.4</td>
      <td>2.9</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



Okay, now we know that our dataframe has five columns, that describe the properties of different species of irises.
_But wait!_, you may ask, _there are [260–300 species of iris genus](https://www.pacificbulbsociety.org/pbswiki/index.php/Iris) and there is no way they can all be represented in our 150 row dataframe!_. Well, my educated friend, you are absolutely right. It might be a good idea to take a look at all the _unique_ values we have in our __Name__ column. To do that we extract our __Name__ column as a Series.


```python
iris_names = iris["Name"]
iris_names
```




    0         Iris-setosa
    1         Iris-setosa
    2         Iris-setosa
    3         Iris-setosa
    4         Iris-setosa
    5         Iris-setosa
    6         Iris-setosa
    7         Iris-setosa
    8         Iris-setosa
    9         Iris-setosa
    10        Iris-setosa
    11        Iris-setosa
    12        Iris-setosa
    13        Iris-setosa
    14        Iris-setosa
    15        Iris-setosa
    16        Iris-setosa
    17        Iris-setosa
    18        Iris-setosa
    19        Iris-setosa
    20        Iris-setosa
    21        Iris-setosa
    22        Iris-setosa
    23        Iris-setosa
    24        Iris-setosa
    25        Iris-setosa
    26        Iris-setosa
    27        Iris-setosa
    28        Iris-setosa
    29        Iris-setosa
                ...      
    120    Iris-virginica
    121    Iris-virginica
    122    Iris-virginica
    123    Iris-virginica
    124    Iris-virginica
    125    Iris-virginica
    126    Iris-virginica
    127    Iris-virginica
    128    Iris-virginica
    129    Iris-virginica
    130    Iris-virginica
    131    Iris-virginica
    132    Iris-virginica
    133    Iris-virginica
    134    Iris-virginica
    135    Iris-virginica
    136    Iris-virginica
    137    Iris-virginica
    138    Iris-virginica
    139    Iris-virginica
    140    Iris-virginica
    141    Iris-virginica
    142    Iris-virginica
    143    Iris-virginica
    144    Iris-virginica
    145    Iris-virginica
    146    Iris-virginica
    147    Iris-virginica
    148    Iris-virginica
    149    Iris-virginica
    Name: Name, Length: 150, dtype: object




```python
type(iris_names)
```




    pandas.core.series.Series




```python
iris_names.unique()
```




    array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)



Now we know that our dataset deals with only three species of iris: [Iris Setosa](https://apps.rhs.org.uk/plantselectorimages/detail/RHS_PUB0001482_1050.JPG), [Iris Versicolor](https://gardengoodsdirect.com/wp-content/uploads/2017/03/Iris_versicolor_3.jpg) and [Iris Virginica](https://plants.ces.ncsu.edu/media/images/Iris-virginica--Justin-Meissen--CC-BY-SA.jpg)

We are going to look at the similarities and differences between the species later, but first, let's get familiar with each of them separately. For that, we can create a separate dataframe for each of the species.


```python
setosa = iris[iris["Name"]=='Iris-setosa']
```

Make sure you understand the line above. In order to do that, disect it bit by bit.
* What does `iris["Name"]` return?
* What does `iris["Name"]=='Iris-setosa'` return? Why? Is this a familiar behaviour?
* What is going to happen when you type `setosa`?

Now you can go ahead and create dataframes for the other two species.


```python

```

If we want to take a closer look at any one of the species-specific dataframes that we now have, a good starting point is the `describe` method of Data Frames (or Series)


```python
setosa.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.00600</td>
      <td>3.418000</td>
      <td>1.464000</td>
      <td>0.24400</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.35249</td>
      <td>0.381024</td>
      <td>0.173511</td>
      <td>0.10721</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.30000</td>
      <td>2.300000</td>
      <td>1.000000</td>
      <td>0.10000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.80000</td>
      <td>3.125000</td>
      <td>1.400000</td>
      <td>0.20000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.00000</td>
      <td>3.400000</td>
      <td>1.500000</td>
      <td>0.20000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.20000</td>
      <td>3.675000</td>
      <td>1.575000</td>
      <td>0.30000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.80000</td>
      <td>4.400000</td>
      <td>1.900000</td>
      <td>0.60000</td>
    </tr>
  </tbody>
</table>
</div>



First thing to note is that `describe()` does not include the __Name__ column. It shows only the _numerical_ data. From this we can see that Iris Setosa is not a very versitile flower: deviations from the mean are quite small and the vast majority of flowers are quite similar in every way with the exception of _Petal Width_, which has outliers about six times the mean width.

Take a look at the other two species. Can you spot anything interesting?


```python

```

Okay, numbers are cool and all, but let's create some _graphs_. Since we mentioned that the _Petal Width_ of Iris Setosa might be interesting to look at, let's look at the histogram.

_(In order to save yourself **A LOT** of time, please start using TAB autocompletion if you haven't already:
Instead of typing `setosa.PetalWidth`, then correcting typos, then realising it's case-sensitive and redoing everything, just do `seto<TAB>`, `.P<TAB>`, `▼ ENTER`)_


```python
setosa.PetalWidth.hist()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdfb53bc898>




![png](output_23_1.png)


Something is clearly wrong with our histogram. It shows the information, sure. But what are those gaps? If you press `SHIFT+TAB` while being inside the parentheses of `hist()`, you can see all the arguments you can provide to it. Not that `bins` has a default value of `10`. Our histogram tries to split the data into ten bins, but our values are between `0.1` and `0.6` and simply do not support that level of granularity.

Try adjusting the number of bins to make the histogram more readable. What number makes more sense than `10` in our case? Why?


```python

```

If there are any other histograms you think are worth looking at, feel free to plot them, too.

But histograms describe the properties of one particular column of a dataframe. And the real power of data science is in seeing relationships between different properties.
Is there a relationship between Sepal Length and Petal Length? Let's find out!


```python
setosa.plot.scatter('SepalLength', 'PetalLength')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdfb509d0b8>




![png](output_27_1.png)


Hmm, doesn't look that related. (Is that the case for all three species?)
What about Sepal Length and Sepal Width?


```python
setosa.plot.scatter('SepalLength', 'SepalWidth')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdfb501f2e8>




![png](output_29_1.png)


Now we are starting to see some relationship! What other variable pairs do you think might be related? Test out your hypotheses.


```python

```

Now that we have played around with three species separately, let's take a look at the whole dataset again.


```python
iris.plot.scatter('SepalLength', 'PetalLength')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdfb4ff2fd0>




![png](output_33_1.png)


We can see a linear relationship between Sepal Length and Petal Length that we couldn't see on Setosa graph. All of the setosa data points are in that bottom-left island of the graph.

We can also squeeze in more information into this graph by utilising colour:


```python
iris.plot.scatter('SepalLength', 'PetalLength', c='PetalWidth', colormap='hsv')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdfb4d652b0>




![png](output_35_1.png)


_(super-extra-cool points if you figure out how to colorise points by species name)_

But wait! There's more!


```python
iris.plot.scatter('SepalLength', 'PetalLength', s=iris["SepalWidth"]**4, c='PetalWidth', colormap='hsv')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdfb4ef9a58>




![png](output_38_1.png)


What is happening in the above cell? Make sure to utilize `SHIFT+TAB` in order to examine what arguments `plot.scatter()` can take. Why is there `**4` all of a sudden? What is going to happen if you change that value?

But what if we want to take a look at _every possible variable pair_? Surely that can't be done in one line, right?


```python
pd.plotting.scatter_matrix(iris, figsize=[10,10])
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2b9fb00>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2af7358>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2b1eda0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2acc860>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2a7c320>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2a7c358>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2a4d860>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb29fd320>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2a21da0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb29d1860>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2980320>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb29a6da0>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2953860>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2901320>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb2926da0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x7fdfb28d6860>]],
          dtype=object)




![png](output_41_1.png)



```python

```
