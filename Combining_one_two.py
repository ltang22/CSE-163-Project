"""
Amuktha Josyula, Natalie Olson, Lily Tang
CSE 163
This file filters and creates visualizations
from a combined dataset of University statistics from the US DOE and Kaggle.
(Datasets 1 and 2)
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def stats(merged: pd.DataFrame):
    """
    This function prints out the statistics for each variable in
    the combined dataset.
    """
    print(merged.isnull().sum())
    print(merged['ADM_RATE'].describe())
    print(merged['Graduate Rate'].describe())
    print(merged['MD_EARN_WNE_P6'].describe())


def visual_one(merged: pd.DataFrame):
    """
    This function creates a scatterplot for the combined dataset.
    """
    plt.figure()
    sns.scatterplot(data=merged, x="ADM_RATE", y="Graduate Rate")
    plt.xlabel("Admission Rate")
    plt.ylabel("Graduation Rate")
    plt.title("Admission Rate vs Graduation Rate")


def visual_two(merged: pd.DataFrame):
    """
    This function creates a line graph for the combined dataset.
    """
    plt.figure()
    sns.lineplot(data=merged, x="Graduate Rate", y="MD_EARN_WNE_P6")
    plt.xlabel("Graduation Rate")
    plt.ylabel("Median Earnings 6 years post graduation")
    plt.title("Graduation Rate vs. MD_EARN_WNE_P6")


def main():
    # Processing and filtering the two datasets
    dataset_2 = pd.read_csv('new.csv')
    dataset_1 = pd.read_csv('kaggle.csv')
    data_2_filtered = dataset_2[['INSTNM', 'ADM_RATE', 'MD_EARN_WNE_P6']]
    data_1_filtered = dataset_1[['University Name', 'Graduate Rate']]

    # Merging the datasets together
    merged = pd.merge(data_2_filtered, data_1_filtered, left_on='INSTNM',
                      right_on='University Name', how='inner')
    merged = merged[['INSTNM', 'ADM_RATE', 'Graduate Rate', 'MD_EARN_WNE_P6']]
    # Turning percentages from strings into ints
    merged['Graduate Rate'] = merged['Graduate Rate'].str.replace('%', '')
    merged['Graduate Rate'] = pd.to_numeric(merged['Graduate Rate'],
                                            errors='coerce')

    # Creating a new CSV file from the merged dataset
    merged.to_csv('combined.csv', index=False)

    # Printing the statistics for the combined dataset
    stats(merged)

    # Running the visualizations
    visual_one(merged)
    visual_two(merged)
    plt.show()


if __name__ == '__main__':
    main()
