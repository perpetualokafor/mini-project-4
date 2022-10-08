# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project is to predict if a customer will get approved for a loan based on some speific informations

## Hypothesis
I hypothesized that applicants with high income and few dependents will get approved for a loan

## EDA 
The higher your income the more likely you will get approved for a loan
Applicants with fewer dependents got approved more
In general, applicants who are graduates had thier loans approved more.


## Process

### Step 1
I analyzed variables to see how they relate with each other 

### Step 2
I then replaced with null values

### Step 3
DecisionTreeClassifier was used for creating the model

### Step 4
Deployed model to cloud using python

## Results/Demo
The model accuracy score was 76%. It was able to accurately predict the first row of the dataset

## Challanges 
Converting my categorical variables. I used labelEncoder which worked fine in training the model but after deploying and trying to read the model, it wouldn't take in categorical data so I had to fix that. 
There also wasn't enough time allocated for this project. I had difficulty deploying to AWS as well.

## Future Goals
When I run my model and enter the values for my json_data, I couldn't get the result to print as 'Y' for loan approved and 'N' for loan not approved. or 1 for loan approved and 0 for loan not approved. i would like to go back and try and fix this