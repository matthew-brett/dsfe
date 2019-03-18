---
layout: single
title: Dataset for DSfE course
permalink: /datasets
---

These are some notes about the datasets contained in the Data Science for Everyone course.

## gender_stats.csv

This dataset is a subset of a larger dataset from the World Bank
on gender and inequality:
<https://data.worldbank.org/data-catalog/gender-statistics>.

The subset is a selection of variables for every country. For
each variable, we have taken the mean of all available values
from 2012 through 2016.

See the `notes` directory of the source repository for the
notebooks that generate the data from the original dataset.

## Country codes etc

The file `un_stats_division_countries.csv` contains information about country
codes and classification. It is a very slightly modified copy of a file
downloaded in March 2019 from the [UN statistics
website](https://unstats.un.org/unsd/methodology/m49/overview).  The
modifications are three single-character edits to replace commas in country
names with semi-colons.
