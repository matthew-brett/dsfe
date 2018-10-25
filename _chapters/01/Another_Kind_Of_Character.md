---
interact_link: notebooks/01/Another_Kind_Of_Character.ipynb
title: '1.3.2 Another Kind of Character'
permalink: 'chapters/01/Another_Kind_Of_Character'
previouschapter:
  url: chapters/01/Literary_Characters
  title: '1.3.1 Literary Characters'
nextchapter:
  url: chapters/02/to_code
  title: '2. Programming'
redirect_from:
  - 'chapters/01/another-kind-of-character'
---

This page is largely derived from `Another_Kind_Of_Character` of the UC
Berkeley course \- see the license file on the main website.

In some situations, the relationships between quantities allow us to make
predictions. This text will explore how to make accurate predictions based on
incomplete information and develop methods for combining multiple sources of
uncertain information to make decisions.

As an example of visualizing information derived from multiple sources, let us
first use the computer to get some information that would be tedious to
acquire by hand. In the context of novels, the word "character" has a second
meaning: a printed symbol such as a letter or number or punctuation symbol.
Here, we ask the computer to count the number of characters and the number of
periods in each chapter of *Pride and Prejudice*.



{:.input_area}
```python
# In each chapter, count the number of all characters;
# Also count the number of periods.
chars_periods = pd.DataFrame.from_dict({
        'Number of chars in chapter': [len(s) for s in book_chapters],
        'Number of periods': np.char.count(book_chapters, '.')
    })
```


Here are the data. Each row of the table corresponds to one chapter of the
novel and displays the number of characters as well as the number of periods
in the chapter. Not surprisingly, chapters with fewer characters also tend to
have fewer periods, in general – the shorter the chapter, the fewer sentences
there tend to be, and vice versa. The relation is not entirely predictable,
however, as sentences are of varying lengths and can involve other punctuation
such as question marks.



{:.input_area}
```python
chars_periods
```





<div markdown="0">
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
      <th>Number of chars in chapter</th>
      <th>Number of periods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4613</td>
      <td>59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4420</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9746</td>
      <td>106</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6045</td>
      <td>54</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5390</td>
      <td>61</td>
    </tr>
    <tr>
      <th>5</th>
      <td>13287</td>
      <td>114</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11492</td>
      <td>111</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11274</td>
      <td>109</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9971</td>
      <td>119</td>
    </tr>
    <tr>
      <th>9</th>
      <td>12798</td>
      <td>126</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9160</td>
      <td>99</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4020</td>
      <td>29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9654</td>
      <td>93</td>
    </tr>
    <tr>
      <th>13</th>
      <td>6576</td>
      <td>58</td>
    </tr>
    <tr>
      <th>14</th>
      <td>9956</td>
      <td>82</td>
    </tr>
    <tr>
      <th>15</th>
      <td>19475</td>
      <td>185</td>
    </tr>
    <tr>
      <th>16</th>
      <td>7436</td>
      <td>69</td>
    </tr>
    <tr>
      <th>17</th>
      <td>29704</td>
      <td>270</td>
    </tr>
    <tr>
      <th>18</th>
      <td>10845</td>
      <td>88</td>
    </tr>
    <tr>
      <th>19</th>
      <td>9374</td>
      <td>108</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11521</td>
      <td>86</td>
    </tr>
    <tr>
      <th>21</th>
      <td>10181</td>
      <td>75</td>
    </tr>
    <tr>
      <th>22</th>
      <td>9807</td>
      <td>85</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11066</td>
      <td>113</td>
    </tr>
    <tr>
      <th>24</th>
      <td>8774</td>
      <td>90</td>
    </tr>
    <tr>
      <th>25</th>
      <td>13227</td>
      <td>126</td>
    </tr>
    <tr>
      <th>26</th>
      <td>7374</td>
      <td>61</td>
    </tr>
    <tr>
      <th>27</th>
      <td>8390</td>
      <td>70</td>
    </tr>
    <tr>
      <th>28</th>
      <td>14010</td>
      <td>127</td>
    </tr>
    <tr>
      <th>29</th>
      <td>7187</td>
      <td>46</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>8652</td>
      <td>78</td>
    </tr>
    <tr>
      <th>32</th>
      <td>10602</td>
      <td>99</td>
    </tr>
    <tr>
      <th>33</th>
      <td>12251</td>
      <td>92</td>
    </tr>
    <tr>
      <th>34</th>
      <td>18487</td>
      <td>130</td>
    </tr>
    <tr>
      <th>35</th>
      <td>12033</td>
      <td>83</td>
    </tr>
    <tr>
      <th>36</th>
      <td>7958</td>
      <td>70</td>
    </tr>
    <tr>
      <th>37</th>
      <td>6080</td>
      <td>47</td>
    </tr>
    <tr>
      <th>38</th>
      <td>8962</td>
      <td>74</td>
    </tr>
    <tr>
      <th>39</th>
      <td>9400</td>
      <td>104</td>
    </tr>
    <tr>
      <th>40</th>
      <td>13260</td>
      <td>110</td>
    </tr>
    <tr>
      <th>41</th>
      <td>11172</td>
      <td>87</td>
    </tr>
    <tr>
      <th>42</th>
      <td>28068</td>
      <td>237</td>
    </tr>
    <tr>
      <th>43</th>
      <td>13622</td>
      <td>90</td>
    </tr>
    <tr>
      <th>44</th>
      <td>10296</td>
      <td>68</td>
    </tr>
    <tr>
      <th>45</th>
      <td>17642</td>
      <td>153</td>
    </tr>
    <tr>
      <th>46</th>
      <td>22976</td>
      <td>180</td>
    </tr>
    <tr>
      <th>47</th>
      <td>12995</td>
      <td>110</td>
    </tr>
    <tr>
      <th>48</th>
      <td>12730</td>
      <td>124</td>
    </tr>
    <tr>
      <th>49</th>
      <td>12922</td>
      <td>111</td>
    </tr>
    <tr>
      <th>50</th>
      <td>11463</td>
      <td>106</td>
    </tr>
    <tr>
      <th>51</th>
      <td>17676</td>
      <td>168</td>
    </tr>
    <tr>
      <th>52</th>
      <td>16463</td>
      <td>185</td>
    </tr>
    <tr>
      <th>53</th>
      <td>9104</td>
      <td>81</td>
    </tr>
    <tr>
      <th>54</th>
      <td>13287</td>
      <td>125</td>
    </tr>
    <tr>
      <th>55</th>
      <td>15712</td>
      <td>163</td>
    </tr>
    <tr>
      <th>56</th>
      <td>9672</td>
      <td>72</td>
    </tr>
    <tr>
      <th>57</th>
      <td>13976</td>
      <td>131</td>
    </tr>
    <tr>
      <th>58</th>
      <td>13952</td>
      <td>149</td>
    </tr>
    <tr>
      <th>59</th>
      <td>9020</td>
      <td>87</td>
    </tr>
    <tr>
      <th>60</th>
      <td>26470</td>
      <td>269</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 2 columns</p>
</div>
</div>



In the plot below, there is a dot for each chapter in the book. The horizontal
axis represents the number of periods and the vertical axis represents the
number of characters.



{:.input_area}
```python
plt.figure(figsize=(6, 6))
plt.scatter(chars_periods['Number of periods'],
            chars_periods['Number of chars in chapter'],
            color='darkblue')
```





{:.output_data_text}
```
<matplotlib.collections.PathCollection at 0x1149f04e0>
```




![png](../../images/chapters/01/Another_Kind_Of_Character_6_1.png)


Notice how the blue points are roughly clustered around a straight line.

Now look at all the chapters that contain about 100 periods. The plot shows
that those chapters contain about 10,000 characters to about 15,000
characters, roughly. That's about 90 to 150 characters per period.

Indeed, it appears from looking at the plot that the chapters tend to have
somewhere between 100 and 150 characters between periods, as a very rough
estimate. Perhaps Jane Austen was announcing something familiar to us now: the
original 140-character limit of Twitter.

{% data8page Another_Kind_Of_Character %}
