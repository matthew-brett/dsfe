---
layout: single
title: Plagiarism rules
permalink: /projects/plagiarism
---

Finding the right way to solve a particular problem often involves looking at
other people's code examples.

You can use code you have found on the web, on two conditions:

* You say where the code came from;
* You comment the code, or use some other way to show that you fully
  understand the code that you have used.

For example, let's say you are trying to read stock prices.  You come across
[this
page](https://streamofconscientia.wordpress.com/2015/01/22/using-pandas-to-get-stock-data).

It has the following code snippet:

```{python}
tickers = ['ORCL', 'TSLA', 'IBM', 'MSFT']
start = datetime(2014,1,1)
end = datetime(2014,12,31)
stockRawData = web.DataReader(tickers, 'yahoo', start, end)
```

If you use this snippet, you should do something like the following in your notebook or Python code:

```{python}
# From:
# https://streamofconscientia.wordpress.com/2015/01/22/using-pandas-to-get-stock-data
# Stock symbols
tickers = ['ORCL', 'TSLA', 'IBM', 'MSFT']
start = datetime(2014,1,1)
end = datetime(2014,12,31)
# Use Yahoo API via Pandas to fetch stock data between given dates
stockRawData = web.DataReader(tickers, 'yahoo', start, end)
```
