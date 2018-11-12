# Notes from the Berkeley textbook

Textbook is [Inferential and Computational
Thinking](https://www.inferentialthinking.com)

## Content

Here's the summary, with annotations

* [Data Science](chapters/01/what-is-data-science.md)
  * [Introduction](chapters/01/1/intro.md)
    * [Computational Tools](chapters/01/1/1/computational-tools.md)
    * [Statistical Techniques](chapters/01/1/2/statistical-techniques.md)
  * [Why Data Science?](chapters/01/2/why-data-science.md)
  * [Plotting the Classics](chapters/01/3/plotting-the-classics.md)
    * [Literary Characters](chapters/01/3/1/literary-characters.md)
    * [Another Kind of Character](chapters/01/3/2/another-kind-of-character.md)
* [Causality and Experiments](chapters/02/causality-and-experiments.md)
  * [John Snow and the Broad Street Pump](chapters/02/1/observation-and-visualization-john-snow-and-the-broad-street-pump.md)
  * [Snow’s “Grand Experiment”](chapters/02/2/snow-s-grand-experiment.md)
  * [Establishing Causality](chapters/02/3/establishing-causality.md)
    Is it just an association?  The idea of a control group.  Comparing groups
    that only differ in the attribute of interest.
  * [Randomization](chapters/02/4/randomization.md)
    Randomization as a way to make a good control group.  Randomized
    controlled trials.  Blind trials.
  * [Endnote](chapters/02/5/endnote.md)
* [Programming in Python](chapters/03/programming-in-python.md)
  * [Expressions](chapters/03/1/expressions.md)
  * [Numbers](chapters/03/2/numbers.md)
  * [Names](chapters/03/3/names.md)
    * [Example: Growth Rates](chapters/03/3/1/example-growth-rates.md)
  * [Call Expressions](chapters/03/4/call-expressions.md)
    Calling functions.  round, max.  Different numbers of arguments.
* [Data Types](chapters/04/data-types.md)
  * [Strings](chapters/04/1/strings.md)
    Adding strings.  Converting numbers to strings with `str`
    * [String Methods](chapters/04/1/1/string-methods.md)
      The idea of a function attached to an object.  `upper`, `replace`.
  * [Comparisons](chapters/04/2/comparisons.md)
    Including boolean variables.  Comparison of strings.
  * [Sequences](chapters/04/3/sequences.md)
    Straight to arrays, with `make_array`.  `sum`.
  * [Arrays](chapters/04/4/arrays.md)
    String and numeric arrays.  Elementwise \* and + with scalars.  `size`,
    `sum`, `mean` methods.  `import numpy as np`.
  * [Ranges](chapters/04/5/ranges.md)
    In fact, `arange`.
  * [More on Arrays](chapters/04/6/more-on-arrays.md)
    Elementwise combination of arrays.
* [Tables](chapters/05/tables.md)
  Creating tables from data.  Loading Minard data table. Adding columns to
  a table.  Number of columns.  Number of rows.  Column names.  Renaming
  columns.  Getting data from columns.  Formatting print output of columns.  Selecting columns.  Dropping columns.
  * [Sorting Rows](chapters/05/1/sorting-rows.md)
    `show` to show some rows.  `sort` by a column. `descending` as a option, and keyword arguments.
  * [Selecting Rows](chapters/05/2/selecting-rows.md)
    By index, integer(s).  By features - `t.where('SALARY'), are.above(10))`.
  * [Example: Population Trends](chapters/05/3/example-trends-in-the-population-of-the-united-states.md)
    Subtracting columns.
  * [Example: Trends in Gender](chapters/05/4/example-gender-ratio-in-the-us-population.md)
    Increasing F:M ratio as a function of age.
* [Visualization](chapters/06/visualization.md)
  IMDB etc databases. Scatter plots, line graphs.
  * [Categorical Distributions](chapters/06/1/visualizing-categorical-distributions.md)
    Ice cream example. Bar charts, particularly horizontal bar charts.
    Sorting categories.
  * [Numerical Distributions](chapters/06/2/visualizing-numerical-distributions.md)
    Histograms.  Bins.  Unequal bins.  Counts vs proportions.  Differences
    between bar charts and histograms.  Grouping.  Numerical variables as categories, and confusion therefrom.
  * [Overlaid Graphs](chapters/06/3/overlaid-graphs.md)
    Categories on scatter plots, histograms, bar charts, line graphs.
* [Functions and Tables](chapters/07/functions-and-tables.md)
  Defining functions. Local scope.  Docstrings.  Multiple arguments.
  * [Applying Functions to Columns](chapters/07/1/applying-a-function-to-a-column.md)
    Functions as values.  Passing a function.  Applying a function to a row of
    data.
  * [Classifying by One Variable](chapters/07/2/classifying-by-one-variable.md)
    Group, then count.  Group and sum, arbitrary functions.
  * [Cross-Classifying](chapters/07/3/cross-classifying-by-more-than-one-variable.md)
    Classifying by more than one variable. `group` again, and `pivot`.
  * [Joining Tables by Columns](chapters/07/4/joining-tables-by-columns.md)
    The `join` method.
  * [Bike Sharing in the Bay Area](chapters/07/5/bike-sharing-in-the-bay-area.md)
    Using various table methods. `datascience` classes `Marker.map_table`,
    `Circle.map_table`.
* [Randomness](chapters/08/randomness.md)
  `np.random.choice`; comparisons, and booleans.  Comparing strings.
  Comparisons in arrays. `count_nonzero`.
  * [Conditional Statements](chapters/08/1/conditional-statements.md)
    `if`, `elif`, `else`, demonstrated inside functions.
  * [Iteration](chapters/08/2/iteration.md)
    `for`, using `np.arange`.  Unrolling loops.  `np.append`.
  * [Simulation](notebooks/09/3/Simulation.ipynb)
    The idea of simulation.  How to simulate.  Heads and tails. Histograms, for
    loops. Rolling two dice in monopoly.
  * [The Monty Hall Problem](chapters/08/3/monty-hall-problem.md)
    Simulations with functions and arrays.
  * [Finding Probabilities](chapters/08/4/finding-probabilities.md)
    Probabilities of combined events - multiplying.  Conditional probabilities.
    Probabilities when there are two different ways of something happening.
* [Sampling and Empirical Distributions](notebooks/10/Sampling_and_Empirical_Distributions.ipynb)
  Random and not-random samples.  Sampling with uneven but known probability.
  Sampling every N, after starting at a random point (_systematic_ sample).
  Sampling with and without replacement.
  * [10.1 Empirical Distributions](notebooks/10/1/Empirical_Distributions.ipynb)
    Theoretical distributions.  Observed distributions.  Law of averages - as the sample number increases, the empirical distribution becomes more like the theoretical.
  * [10.2 Sampling from a Population](notebooks/10/2/Sampling_from_a_Population.ipynb)
    Distribution of a random samples from population becomes more like
    distribution of population, as sample size increases.
  * [10.3 Empirical Distibution of a Statistic](notebooks/10/3/Empirical_Distribution_of_a_Statistic.ipynb)
    Numerical quantities from a population = *parameters*. Numerical quantities
    from samples: *statistics*.  Statistic != Parameter.  How different could
    it have been?
* [11. Testing Hypotheses](notebooks/11/Testing_Hypotheses.ipynb)
  Answers for yes/no questions from data.
  * [11.1 Assessing Models](notebooks/11/1/Assessing_Models.ipynb)
    Model == "a set of assumptions about data".  Statistic.  Predicting
    statistic under the model.  Compare prediction and data.  Swain's jury.
    Mendel's flowers.
  * [11.2 Multiple Categories](notebooks/11/2/Multiple_Categories.ipynb)
    Race from California jury selections.  Total variation distance as measure of distance between distributions.  Simulating jurors, and variation distances.  Explanations for failure of model.
  * [11.3 Decisions and Uncertainty](notebooks/11/3/Decisions_and_Uncertainty.ipynb)
    Null-hypothesis, alternative hypothesis, test statistic, distribution under
    the null, conclusion.  How to decide whether statistic is too unusual.
    Ronald Fisher and 0.05.
* [12. Comparing Two Samples](notebooks/12/Comparing_Two_Samples.ipynb)
  Instead of comparing sample to known population.
  * [12.1 A/B Testing](notebooks/12/1/AB_Testing.ipynb)
    Mean difference of birth weights to smokers / non-smokers.  Permutation.
  * [12.2 Deflategate](notebooks/12/2/Deflategate.ipynb)
    Permutation test for Deflategate pressure measurements.
  * [12.3 Causality](notebooks/12/3/Causality.ipynb)
    Proportion of patients with pain relief from Botulinum toxin.  Random assignment of patients.  Permutation test of proportions. Difficulty of drawing firm conclusions.
* [13. Estimation](notebooks/13/Estimation.ipynb)
  Sample statistic to estimate parameter.  "How different could this estimate
  have been, if the sample had come out differently?"
  * [13.1 Percentiles](notebooks/13/1/Percentiles.ipynb)
    Calculating percentiles.  Quartiles.
  * [13.2 The Bootstrap](notebooks/13/2/Bootstrap.ipynb)
    Bootstrap for estimating variability of statistic.  Salaries in SF.
    Estimate of median from sample using bootstrap.  Do estimates *capture* the
    parameter.
  * [13.3 Confidence Intervals](notebooks/13/3/Confidence_Intervals.ipynb)
    Bootstrap for 95% (etc) confidence intervals, mean baby birth weight.  Bootstrap for proportions.  Caveats for bootstrap.
  * [13.4 Using Confidence Intervals](notebooks/13/4/Using_Confidence_Intervals.ipynb)
    Testing whether a parameter is plausible.  Hodgkin's Lymphoma, comparing drop in lung function over time, after treatment.  Comparing drop to 0, using confidence intervals.
* [14. Why the Mean Matters](notebooks/14/Why_the_Mean_Matters.ipynb)
  Empirical distribution of mean is generally normal.
  * [14.1 Properties of the Mean](notebooks/14/1/Properties_of_the_Mean.ipynb)
    Mean as "smoother".  Depends only on distribution of values (not numbers).  Balance point of histogram.  Relationship of median and mean.
  * [14.2 Variability](notebooks/14/2/Variability.ipynb)
    Deviations from average.  Squared deviations.  Mean squared deviation ==
    variance -> SD.  Most observations are a few standard SDs from the mean.  Chebychev.
  * [14.3 The SD and the Normal Curve](notebooks/14/3/SD_and_the_Normal_Curve.ipynb)
    Point of inflection.  Standard units, and the standard normal curve.  The CDF.  Proportion of area between +/-1 and 2 SDs.
  * [14.4 The Central Limit Theorem](notebooks/14/4/Central_Limit_Theorem.ipynb)
    Simulation of sum of red / black choice in red -> normal.  Average flight
    delay (where flight delay is positive-skewed).  Proportion of purple flowers in Mendel's data.  Width of sampling distribution as a function of sample size.  No relationship to population size.  Large samples make result valid for any distribution.
  * [14.5 The Variability of the Sample Mean](notebooks/14/5/Variability_of_the_Sample_Mean.ipynb)
    Width of sampling distribution, sample size.  Root N as scaling for SD.
  * [14.6 Choosing a Sample Size](notebooks/14/6/Choosing_a_Sample_Size.ipynb)
    Using SDs to predict confidence intervals, and therefore, required sample size for given levels of confidence.
* [15. Prediction](notebooks/15/Prediction.ipynb)
  Predicting child height (y) from parents' height (x), by averaging over x
  intervals.
  * [15.1 Correlation](notebooks/15/1/Correlation.ipynb)
    MPG / acceleration data.  Changing to standard units.  Correlation and
    scatter, in standard units.  "r measures the extent to which the scatter
    plot clusters around a straight line".  r and the dot product of x, y in standard units.  Not causation.  Only measures linear association.
  * [15.2 The Regression Line](notebooks/15/2/Regression_Line.ipynb)
    The regression line and the 45 degree line.  Regression slope from
    correlation coefficient.   Prediction from the regression line.  Meaning of the regression slope.
  * [15.3 The Method of Least Squares](notebooks/15/3/Method_of_Least_Squares.ipynb)
    "Best" line.  Line, predictions, and prediction error.  Root mean squared
    error.  Trying different lines.  Regression line as best in terms of RMSE.  Finding the line by numerical optimization.
  * [15.4 Least Squares Regression](notebooks/15/4/Least_Squares_Regression.ipynb)
    Shot-put weight lift / shot put distance correlation.  Least squares line still least squares line, even if plot is not rugby-ball shaped.  Find quadratic line using `minimize`.
  * [15.5 Visual Diagnostics](notebooks/15/5/Visual_Diagnostics.ipynb)
    Plotting residuals against parents' heights.  Good regression -> "no pattern" the residuals.  Residual plot of whale length and age reveals non-linearity in data.  Heteroscedasticity ("uneven spread").  Acceleration (x) vs MPG (y).  Residuals more variable for lower acceleration.  Regression estimates less accurate for lower acceleration values.
  * [15.6 Numerical Diagnostics](notebooks/15/6/Numerical_Diagnostics.ipynb)
    x vs residual plot has slope (very near) 0.  Average of residuals always 0.  SD of residuals predictable from SD of y and r.
* [16. Inference for Regression](notebooks/16/Inference_for_Regression.ipynb)
  From regression line in sample to inference on the population.
  * [16.1 A Regression Model](notebooks/16/1/Regression_Model.ipynb)
    Regression model as true line plus random noise.  Generating some points
    from the true line.  The regression line as estimate.  
  * [16.2 Inference for the True Slope](notebooks/16/2/Inference_for_the_True_Slope.ipynb)
    Bootstrapping the regression line. 95% confidence interval.  Non-zero
    regression slope when true line has slope 0.   Inference on the slope with
    null of 0.
  * [16.3 Prediction Intervals](notebooks/16/3/Prediction_Intervals.ipynb)
    Bootstrap regression to get prediction intervals for all points on line.
* [17. Classification](notebooks/17/Classification.ipynb)
  Examples of classifiers (fraudulent orders, compatible matches for dating
  websites, diagnosis of cancer, predicting votes.  Observations.  Attributes.
  Class (fraudulent, not-fraudulent).  Training and testing sets. Can be imperfect.
  * [17.1 Nearest Neighbors](notebooks/17/1/Nearest_Neighbors.ipynb)
    Kidney disease.  Hemoglobin, glucose.  Classify new point.  Nearest
    neighbor.  Decision boundary.  More difficult classifier - WBC and glucose.  k nearest neighbors.
  * [17.2 Training and Testing](notebooks/17/2/Training_and_Testing.ipynb)
    Testing against unknown points - the testing set.  Problem of testing nearest neighbor classifier on training set.  Split data in half.
  * [17.3 Rows of Tables](notebooks/17/3/Rows_of_Tables.ipynb)
    Rows as attributes of observations.  Making rows into arrays.  Pythagoras
    and Euclidean distance.  Distance function.  Applying functions to rows in
    table with `apply`.  Apply "distance to new point" function.  Select top five rows for this distance.  Take majority vote on classification.
  * [17.4 Implementing the Classifier](notebooks/17/4/Implementing_the_Classifier.ipynb)
    Classifying banknotes.  Complex patterns of class on scatterplot. Three attributes and Pythagoras.  More than three.  Distance function for N-D.  Wine dataset, classifying grape species.  General k-nearest neighbors classifier.
  * [17.5 The Accuracy of the Classifier](notebooks/17/5/Accuracy_of_the_Classifier.ipynb)
    Hold-out method (splitting into test and training).  95% prediction success
    for test set.  Breast cancer, school competition.  kNN classifier.  96% accuracy.
  * [17.6 Multiple Regression](notebooks/17/6/Multiple_Regression.ipynb)
    House prices in Iowa.  Prediction with slopes for each predicting variable. RMSE as criterion.  Use `minimize` to find best slopes for training set.  Residual plot - underestimation of high priced houses.  kNN prediction (average of price of the kNNs).
* [18. Updating Predictions](notebooks/18/Updating_Predictions.ipynb)
  * [18.1 A "More Likely Than Not" Binary Classifier](notebooks/18/1/More_Likely_than_Not_Binary_Classifier.ipynb)
    Bayes rule, students in second and third years, majors declared or not.  The tree diagram.
  * [18.2 Making Decisions](notebooks/18/2/Making_Decisions.ipynb)
    False positives, false negatives.  Test for rare disease with low false positive rate.  Table expressing known probabilities to demonstrate Bayes rule.  Effect of priors (subjective probability).

## Homework

For example, see
<https://github.com/data-8/data8assets/blob/gh-pages/materials/su17>.

## Datasets

* [Larry Winner's dataset list](http://users.stat.ufl.edu/~winner/datasets.html).
* <https://medium.com/datadriveninvestor/the-50-best-public-datasets-for-machine-learning-d80e9f030279>.
