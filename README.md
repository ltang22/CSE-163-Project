In order to run this project, you will need to import Kagglehub, which is a python library to interact with Kaggle datasets. You will also need to download pandas, matplotlib.pyplot, and seaborn. The library bokeh will also need to be downloaded.

### DataSet 1

This file examines and generates graphs based on the content in the kagglehub US Universities & Colleges Dataset (2025). It reads in the file and computes variable statistics for our chosen variables of interest. It also creates two seaborn graphs that examine factors of university prestige against student success. It helps break down and evaluate the data of universities to answer our research question and is later combined with another dataset to find true correlations. It can be run to summarize and clean the data in the chosen dataset.

### DataSet 1 Test 

This file tests the dataset1 file by creating a small test file and using assert statements to make sure the methods are working correctly. It can be run to check that methods are working correctly and the dataset is being accurately read and cleaned.

## DataSet 2

This file examines and generates graphs based on the content of the U.S. Department of Education Scorecard Most recent institutions dataset. It reads in the file and computes variable statistics for our chosen variables of interest. It also creates two seaborn graphs that examine factors of university prestige against student success. It helps break down and evaluate the data of universities to answer our research question and is later combined with another dataset to find true correlations. It can be run to summarize and clean the data in the chosen dataset.

## DataSet 2 Graphing

This file creates two graphs based on dataset 2 comparing the university prestige factors with student success variables. It can be run to visualize connections between the variables within dataset 2 and draw conclusions based on the statistics given. 

## Dataset 3

This file examines and generates graphs based on the content in the kagglehub College Completion and Efficiency Measures for US. It reads in the file and computes variable statistics for our chosen variables of interest. It also creates two seaborn graphs that examine factors of university prestige against student success. It helps break down and evaluate the data of universities to answer our research question and is later combined with another dataset to find true correlations. It can be run to summarize and clean the data in the chosen dataset.

## Merged Dataset 1

This file merges the  College Completion and Efficiency Measures for US  and  U.S. Department of Education Scorecard Most recent institutions datasets. It does it based on each university and combines the variables of interest. It is used to visualize and determine any correlation between variables of interest between each university in both datasets. It can be run to see the correlations between different university prestige factors that other datasets may not have and compare it with the student success rates from another dataset. 

## Merged Dataset 2 

This file merges the US Universities & Colleges Dataset (2025) and  U.S. Department of Education Scorecard Most recent institutions datasets. It does it based on each university and combines the variables of interest. It is used to visualize and determine any correlation between variables of interest between each university in both datasets. It can be run to see the correlations between different university prestige factors that other datasets may not have and compare it with the student success rates from another dataset. 

## Steps to run the files:
1. install [Download env.yaml](./path/to/env.yaml) and input the command conda create -f env.yaml into the terminal
2. download and install kagglehub, pandas as pd, matplotlib.py as plt and seaborn as sns
3. run the code of dataset 1 and dataset 1 test 
4. run the code of dataset 2 
5. run the code of dataset 3 
6. run the codes for merged dataset 1 and dataset 2
7. evaluate the merged data and the original summary statistics for each dataset to find correlations between variables of interest and corresponding outcome variables.