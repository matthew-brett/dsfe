---
layout: single
title: Project grading rubric
permalink: /projects/rubric
---

DSFE 2018 project grading rubric
================================

Your total project mark is out of 100.  This mark in turn makes up 70% of your
course grade.

There are two components to this assessment: the project and your
contribution. 72% of the project marks are for the project itself; see
the categories below.

28% of the marks are for your contribution; see heading below.

## Project grades

Each of the following 8 sections is worth 9 marks, for a total of 72.

For each row, the table gives a description of work that will earn: between
0 and 50% in this category (fail to bare pass); 50-75% (bare pass to good
pass); and 75-100% (good pass to excellent).

Notice that your project presentation is one category; see [the project
page](../project) for schedule.

<!---
https://divtable.com/converter/
-->

<table style="width: 1020.45px;"><colgroup> <col style="width: 12%;" /> <col style="width: 28%;" /> <col style="width: 29%;" /> <col style="width: 29%;" /> </colgroup>
<tbody>
<tr class="odd">
<td style="width: 124px;">&nbsp;</td>
<td style="width: 291px;">0-50%</td>
<td style="width: 301px;">50-75%</td>
<td style="width: 301.45px;">75-100</td>
</tr>
<tr class="even">
<td style="width: 124px;">Questions</td>
<td style="width: 291px;">Questions overly simplistic, unrelated, or unmotivated</td>
<td style="width: 301px;">Questions appropriate, coherent, and motivated</td>
<td style="width: 301.45px;">Questions well motivated, interesting, insightful, and novel</td>
</tr>
<tr class="odd">
<td style="width: 124px;">Analysis</td>
<td style="width: 291px;">Choice of analysis is overly simplistic or incomplete</td>
<td style="width: 301px;">Analysis appropriate</td>
<td style="width: 301.45px;">Analysis appropriate, complete, advanced, and informative</td>
</tr>
<tr class="even">
<td style="width: 124px;">Results</td>
<td style="width: 291px;">
<p>Conclusions are missing, incorrect, or not based on analysis</p>
<p>Inappropriate choice of plots; poorly labeled plots; plots missing</p>
</td>
<td style="width: 301px;">
<p>Conclusions relevant, but partially correct or partially complete</p>
<p>Plots convey information but lack context for interpretation</p>
</td>
<td style="width: 301.45px;">
<p>Relevant conclusions explicitly tied to analysis and to context</p>
<p>Plots convey information correctly with adequate and appropriate reference information</p>
</td>
</tr>
<tr class="odd">
<td style="width: 124px;">Code review</td>
<td style="width: 291px;">Little evidence that group members are giving constructive feedback on each other's code.</td>
<td style="width: 301px;">Some evidence that group members are giving constructive feedback on each other's code, leading to better code.</td>
<td style="width: 301.45px;">Extensive evidence that group members are giving constructive feedback on each other's code, leading to better code.</td>
</tr>
<tr class="odd">
<td style="width: 124px;">Readability</td>
<td style="width: 291px;">Code is messy and poorly organized; unused or irrelevant code distracts when reading code. Variables and functions names do not helpful to understand code.</td>
<td style="width: 301px;">Code is reasonably well organized.&nbsp; There is little unused or irrelevant code, or this code has been moved out of the main project files.&nbsp; Variable and function names generally meaningful and helpful for understanding.</td>
<td style="width: 301.45px;">Code very well organized.&nbsp; No irrelevant or distracting code.&nbsp;&nbsp; Variable and function names have clear relationship to their purpose in the code.&nbsp; Code is easy to read and understand.</td>
</tr>
<tr class="odd">
<td style="width: 124px;">Presentation</td>
<td style="width: 291px;">
<p>Verbal presentation is illogical, incorrect, or incoherent.</p>
<p>Visual presentation is cluttered, disjoint, or illegible</p>
<p>Verbal and visual presentation unrelated</p>
</td>
<td style="width: 301px;">
<p>Verbal presentation partially correct but incomplete or unconvincing</p>
<p>Visual presentation is readable and clear</p>
<p>Verbal and visual presentation related</p>
</td>
<td style="width: 301.45px;">
<p>Verbal presentation is correct, complete, and convincing</p>
<p>Visual presentation is appealing, informative, and crisp</p>
<p>Verbal and visual presentation clearly related</p>
</td>
</tr>
<tr class="even">
<td style="width: 124px;">Writing</td>
<td style="width: 291px;">Explanation is illogical, incorrect, or incoherent</td>
<td style="width: 301px;">Explanation is correct, complete, and convincing</td>
<td style="width: 301.45px;">Explanation is correct, complete, convincing, and elegant</td>
</tr>
<tr class="odd">
<td style="width: 124px;">Reproduciblity</td>
<td style="width: 291px;">Code didn't run</td>
<td style="width: 301px;">Recipes in project directory correctly load data and generate all results and figures in report</td>
<td style="width: 301.45px;">Recipes additionally validate data against its source (such as URL or other download). The recipes generate all exploratory work and supplementary analysis</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

## Project report

Your project report should be around 3000 words of explanatory text
and code, not including figures and tables.

It can be in the form of a PDF document, or a Jupyter Notebook.

Your project report should be *reproducible*.  There should be a file
in your project, called `README`, in any format of your choosing. For
example, the file can be in plain text format, a Jupyter Notebook, or
a Word-processor document.

This file should give the steps which will exactly reproduce the
numbers, tables and figures in your report.

Example instructions for a simple report might be:

> The UK police publish various statistics about their work at
> <https://data.police.uk/data>.
>
> Go to this site, select "August 2018" as the start and end of the "Date
> range", select "West Midlands" in the "Forces" panel, unselect "include
> crime data" and select "include stop and search data".  Download
> and unpack the generated zip file, to give the file
> `2018-08-west-midlands-stop-and-search.csv`.  This should exactly match the
> copy of the data in our project directory, with the same name.
>
> Open `clean_data.ipynb` and run all cells.  This checks and cleans the data,
> writing out the cleaner version as `2018-08-wm-ss-cleaned.csv`.
>
> Open `analyze_data.ipynb` and run all cells.  This writes out the figures
> `figure1.png` and `figure2.png` that you see in our report.
>
> Open `simulate_data.ipynb` and run all cells.  This writes out tables 1 and 2
> that you see in our report.

The `README` file can also be your report.  In that case, your
`README` instructions would be "Run this notebook to generate our
report".

## Personal contribution

Each team member should submit a document of up to 1500 words describing their
contribution to the project, under any of the following headings:

* Development of question / hypothesis;
* Data research: search for relevant data to contribute to question;
* Literature review;
* Analysis strategy;
* Analysis code;
* Code review;
* Work planning and organization;
* Improving teamwork and collaboration;
* Testing code and procedures;
* Writing report.

You should describe your own contribution, and any work you did to help other
people contribute to the same area.

You can add other headings if you think we should consider them.

For each heading, give any evidence for your contribution from project files or other data that is accessible to us, your graders.

The mark guidelines for this part are:

* 0-50%: little evidence of contribution or collaboration.  Contributions under
  few headings.  Little effort to help other team members contribute.
* 50-75%: moderate evidence of contribution and collaboration.  Contributions
  under many headings; substantial contributions to more than one heading.
  Evidence that you helped other team members contribute across some headings.
* 75-100%: strong evidence of contribution and collaboration.  Some
  contribution to nearly all headings; substantial contributions across the
  majority of headings.  Strong evidence that you helped other team members contribute across several headings.
