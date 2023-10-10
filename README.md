# Datanic
## Introduction
Datanic is a data science project to share my Pandas and Matplotlib skills.
I'm a huge fan of the Titanic (Olympic) Story. So I wanted to use a Titanic dataset to see which passengers were the most likely to get rescued.

## Steps
  * Firstly I needed to clean the Data. For that, I dropped all the data that didn't have any impact on the outcome.
  * Then I removed all the passengers with unknown ages and passengers that didn't embark
  * Lastly I printed the outcome by grouping people by sex and passenger class.
## Output
Then if we start the programm, it outputs this:

**    sex    pclass  survived  age                   
      female 1       0.962406  37.037594
             2       0.893204  27.499191
             3       0.473684  22.185307
      male   1       0.350993  41.029250
             2       0.145570  30.815401
             3       0.169054  25.962273 **

As we can see women were much more likely to get rescued. 96% for women in first class, 47% for women in second third class, and 35% for men in first class.
But we can also remark something interesting: Men were more likely to get rescued if they were in third class rather than second class (17% vs 15%)
