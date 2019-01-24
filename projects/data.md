---
layout: single
title: Data for projects
permalink: /projects/data
---

# Data for projects

## Don't worry, but take it seriously

Your task is open-ended task, and this is typical of real data analysis
projects.  Each project will go in a different direction, and you will find
that your group will become experts in interpreting your own data.  You might
even end up writing a little paper from your report.

That's the good part.  The bad part is, as in real data analysis, when you
start, it will seem a bit daunting, and it will not be clear where you are
going to end up.  Hold on tight, and keep analyzing to try and understand what the data means, and the conclusions you can make.  You will find that doing this will take you on journeys that you didn't expect.

## General advice

*   Prefer open data - data that can be freely downloaded, preferably
    with an open license, allowing you to share the data freely.
*   Prefer data for which your Data person has some background.
*   Prefer open-ended questions.
*   Fresh data and / or analysis.
*   We will make allowance for your ambition in marking.

The primary rule is that you and your group will be doing a significant exploration of a dataset.  Your exploration should be your own work.

It is OK to chose a dataset that has been analyzed by others, but you should
either show that the analysis and exploration you plan has not been done
before, or show that there is no code already available to do the analysis you intend.

For example, you might be interested in the data from a paper or a report. You
might want to replicate the findings in the paper or report, and then extend
them.  This is fine, unless the paper or report, or some other writer, has
already published code to do a significant amount of the analysis work.

## Ideas for finding datasets

Feel free to use data from your own discipline.  Ask around to see if you can
find interesting data from the University of Birmingham, maybe in your School.

Below there are some links to find datasets.  Try them and see if you can find
something that interests you.

If you find a dataset you cannot load - for example, a dataset that is not in CSV format, and that Pandas cannot easily handle, get your instructors to help, something is always possible.

* [Kaggle datasets](https://www.kaggle.com/datasets).  Kaggle is famous for
  various data science competitions, but it has a large list of datasets.  You will find that many of these already have published analyses, so be careful to check what's out there, or chose something that has not been done before.
* [Google dataset search](https://toolbox.google.com/datasetsearch).  Try the
  link, you'll get the idea.
* [World Bank data](https://data.worldbank.org). The site has a lot of data on
  global development, and related issues.  The `gender_data.csv` dataset we
  have been using is a processed version of
  [https://data.worldbank.org/data-catalog/gender-statistics](https://data.worldbank.org/data-catalog/gender-statistics).
* [UK government open data](https://data.gov.uk).
* [Project Gutenberg](https://www.gutenberg.org/wiki/Main_Page) \- full text of
  many books.
* [UK data service](https://www.ukdataservice.ac.uk/get-data/key-data) "The UK
  Data Service collection includes major UK government-sponsored surveys,
  cross-national surveys, longitudinal studies, UK census data, international
  aggregate, business data, and qualitative data."

## Your pitch

When pitching or justifying your data, think on these headings:

* Where is the data?  Is it easily accessible?  Is it public?  Is it open (can
  you share your copies of the data)?   For extra points, consider reading the data into a notebook and doing some very basic exploration.
* What might the data tell us?  What would you like to explore first?  Can you
  test an idea, or check a previous finding?  Can you come up with a new finding?

For example, let's say I wanted to pitch an analysis of the [West Midlands Fire
Service
data](https://data.birmingham.gov.uk/dataset/wmfs-incident-data-since-2009).

I would start by pointing to the website, as above.

Then I would briefly describe what data is available, ideally by loading the
data into a data frame, and showing the table, and the columns in the table.

In this case, I notice that I have fire incident data from 2009 through 2018.
These are incidents to which the fire service have responded with their
location and outcome.  I might be interested in whether I can detect any signs
of the austerity measures in the response to fire incidents.  Looking at the
variables, I see that number of firemen in various ranks that attend each call.
Has this changed over time, and can this be related to the budget of the fire
service?  Might this differ between incidents in Solihull and Cental
Birmingham?  The data records injuries and deaths.  Have these changed over the period covered?   Is that change the same for different areas of Birmingham?
