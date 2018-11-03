---
layout: single
title: Assignment 5
permalink: /assignments/assignment_5
redirect_from: /assignment_5
---

# Assignment 5

For this assignment, you will need the background from these pages:

* [3.7 Arrays and axes](../chapters/03/arrays_and_axes)
* [3.8 Reply to the Supreme Court](../chapters/03/reply_supreme)

At the time I wrote this, you can find the following on the [Wikipedia
page for Burkitt's
Lymphoma](https://en.wikipedia.org/wiki/Burkitt%27s_lymphoma#Prognosis).

> The overall cure rate for Burkitt's lymphoma in developed countries is
> about 90%, but worse in low-income countries. Burkitt's lymphoma is
> uncommon in adults, where it has a worse prognosis {%cite
> molyneux2012burkitt %}
>
> In 2006, treatment with dose-adjusted EPOCH with Rituximab showed
> promising initial results in a small series of patients (n=17), with
> a 100% response rate, and 100% overall survival and progression-free
> survival at 28 months (median follow-up) {%cite dunleavy2006novel %}

How likely is it that these study results, or better, could have come
about by chance?

Use the tools that you see in [Reply to the Supreme
Court](../chapters/03/reply_supreme).  You might consider copying that
notebook to start.

You can use the tools like this:

* Your model is that the EPOCH study was, in fact, no more effective
  than any other standard therapy, and that they were just lucky, in finding that 100% of their patients were cured.
* You are going to do a simulation, using this model.  In this
  simulation, you will make 17 simulated patients, each with a 90%
  chance of being cured.  Then count how many of the 17 patients were
  cured.
* Do this many times, to see how likely you are to get the value 17 / 17
  (100%).

For extra points - imagine that there were 10 labs doing this exact same
study, but the labs that didn't get results as good as this, did not
publish. In that case, this publication would have been the best of 10
tries to get good results.  If that was so, what are the chances of
seeing results as good as these, or better?

## References

{% bibliography --cited %}
