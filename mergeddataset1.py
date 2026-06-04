'''
Lily Tang, Natalie Olson, Amuktha Josyula
CSE 163
This program combines the datasets: "U.S. Universities and Colleges Dataset
2025" and "College Completion and Efficiency Measures for U.S. Institutions"
to analyze the relationship between admission rates, awards, and SAT scores for
U.S. universities and colleges. It includes functions to calculate
statistics on the merged dataset and create visualizations comparing
admission rates with awards and SAT scores.
'''

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path = kagglehub.dataset_download("thedevastator/college-completion-"
                                  "and-efficiency-measures-for-u")


def merged_stats(merged: pd.DataFrame):
    '''
    Takes in the merged DataFrame and prints out the statistics of the 
    admission rates and awards for each institution
    '''
    print("Merged rows: ", len(merged))
    print("Merged columns: ", len(merged.columns))
    print("Missing values: ", merged.isnull().sum())
    print(merged['ADM_RATE'].describe())
    print(merged['awards_per_value'].describe())
    print(merged['SAT_AVG'].describe())


def plot_acc_rate_and_awards(merged: pd.DataFrame):
    '''
    Takes in the merged DataFrame and creates a scatter plot of the
    admission rates and awards for each institution
    '''
    sns.scatterplot(data=merged, x='ADM_RATE', y='awards_per_value')
    plt.title('Admission Rates vs Awards')
    plt.xlabel('Admission Rate')
    plt.ylabel('Awards')
    plt.show()


def plot_acc_rate_and_sat(merged: pd.DataFrame):
    '''
    Takes in the merged DataFrame and creates a scatter plot of the
    admission rates and SAT scores for each institution
    '''
    sns.scatterplot(data=merged, x='ADM_RATE', y='SAT_AVG')
    plt.title('Admission Rates vs SAT Scores')
    plt.xlabel('Admission Rate')
    plt.ylabel('Average SAT Score')
    plt.show()


def main():
    recent_institutions = pd.read_csv("Most-Recent-Cohorts-Institution.csv")
    college_completion = pd.read_csv(f'{path}/cc_institution_details.csv')
    new_recent_institutions = recent_institutions[['INSTNM', 'ADM_RATE',
                                                   'SAT_AVG']]
    new_college_completion = college_completion[['chronname',
                                                 'awards_per_value']]
    merged = pd.merge(new_recent_institutions, new_college_completion,
                      left_on='INSTNM', right_on='chronname', how='inner')
    merged = merged[['INSTNM', 'ADM_RATE', 'awards_per_value', 'SAT_AVG']]

    merged_stats(merged)
    plot_acc_rate_and_awards(merged)
    plot_acc_rate_and_sat(merged)


if __name__ == "__main__":
    main()
