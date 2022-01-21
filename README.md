# ACM Research Coding Challenge (Spring 2022)

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-S22`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uTpjeA8G).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#question-one)Question One

[Binary classification](https://en.wikipedia.org/wiki/Binary_classification) is a type of classification task that labels elements of a set (i.e. dataset) into two different groups. An example of this type of classification would be identifying if people had a specific disease or not based on certain health characteristics. The dataset found in `mushrooms.csv` holds data (22 different characteristics, specifically) about different types of mushrooms, including a mushroom's cap shape, cap surface texture, cap color, bruising, odor, and more. Remember to split the data into test and training sets (you can choose your own percent split). Information about the meaning of the letters under each column can be found within the file `attributelegend.txt`.

**With the file `mushrooms.csv`, use an algorithm of your choice to classify whether a mushroom is poisonous or edible.**

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library or API you want to implement this, just document which ones you used in this README file.** Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

# SOLUTION:

Multi-class classification (including binary classification) can be performed using [Support Vector Machines](https://www.reddit.com/r/MachineLearning/comments/15zrpp/please_explain_support_vector_machines_svm_like_i/), which is supported in the scikit-learn modules. I've worked with pandas and scikit-learn before, so I'll stick to those as well for this challenge.

Maybe it's because I'm more familiar with it now, but I found this to be much easier. My old hand-me-down laptop still crashes half the time trying to run this thing, though.

Essentially, just separate the 22 attributes into one dataframe and the one-column classification of poisonous/edible into one dataframe, split into testing and training sets, feed that into a Support Vector Classification from [sklearn.svm](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), predict the test data, and print out a confusion matrix and classification report.

As SVC() does not work with strings, [pandas.get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html) is needed to create a one-hot encoding of the data. To demonstrate, if we use get_dummies on the column gill_spacing from mushrooms.csv, which has three possible values of c, w, d, then a dataframe consisting of 3 columns (c,w,d) and 8125 rows (there are 8125 mushrooms) will be generated, with each row having only a single cell with the value of 1 -- in the column corresponding to whatever of the three possible values was present in gill_spacing each individual row.

There are two values of poisonous "p" and edible "e" for the column named 'class' in mushrooms.csv, which means that applying pandas.get_dummies to the 'class', will return a 2-column (p,e) 8125-row dataframe , which prevents us from using the SVC for binary classification; since a value of 1 in a column of this dataframe means a value of 0 in the only other column of this dataframe, we can ignore the poisonous 'p' column of the dataframe to proceed with the binary classification without losing any information.

There are various [kernel types](https://scikit-learn.org/stable/modules/svm.html#svm-kernels) you may use to tailor the algorithm, but I only saw a minor difference in accuracy when using the 'sigmoid' kernel type. Otherwise, the accuracy was near 100%. I split the dataset into 70% training and 30% testing, and tweaking this ratio lead to minor differences in performance as well.

![bloop](https://media.discordapp.net/attachments/803697311871270934/933997040206221312/unknown.png)
