'''
Lily Tang
CSE 163 AJ
This program analyzes a dataset of U.S. universities and colleges from 2025 on
kaggle. It provides insights into the data, including the number of
rows, missing values, and statistics on graduate rates,
locations, types, groups, and earnings. It also generates 2
visualizations comparing earnings with graduaterates and types of institutions.
'''

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download latest version
path = kagglehub.dataset_download(
    "brahmendrajayaraju/u-s-universities-and-colleges-dataset-2025")

print("Path to dataset files:", path)

df = pd.read_csv("universities_data.csv")


def rows(df: pd.DataFrame) -> int:
    '''
    Takes in the dataframe with the dataset and returns the
    number of rows in the dataframe.
    '''
    return len(df)


def missing_values_and_columns(df: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns
    a series of the number of missing values in each
    column of the dataframe.
    '''
    return df.isnull().sum()


def graduate_rate_stats(df: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns a series
    with the IQR, mean, median, max, min, and standard deviation of
    the graduate rates
    '''
    df['Graduate Rate'] = df['Graduate Rate'].str.rstrip('%').astype(float)
    return df['Graduate Rate'].describe()


def location_stats(df: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns a series of
    the number of unique values, top value, and frequency of the top value
    for the location column.
    '''
    return df['Location'].describe()


def type_stats(df: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns a series of
    the number of unique values, top value, and frequency of the top value
    for the type column.
    '''
    return df['Type'].describe()


def group_stats(df: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns a series of
    the number of unique values, top value, and frequency of the top value
    for the group column.
    '''
    return df['Group'].describe()


def earnings_stats(df: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns a series of
    the IQR, mean, median, max, min, and standard deviation of the earnings
    '''
    df['Earnings'] = df['Earnings'].str.replace('$', '')
    df['Earnings'] = df['Earnings'].str.rstrip('k').astype(float) * 1000
    return df['Earnings'].describe()


def graduate_rate_earnings_graph(df: pd.DataFrame):
    '''
    Creates a scatter plot comparing graduate rates on the x-axis
    and earnings on the y-axis for the universities in the data set
    '''
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Graduate Rate', y='Earnings', data=df)
    plt.title('Graduate Rate vs. Earnings')
    plt.xlabel('Graduate Rate (%)')
    plt.ylabel('Earnings ($)')


def type_earnings_graph(df: pd.DataFrame):
    '''
    Creates a box plot displaying graduate earnings on the y-axis 
    and the type of institution on the x-axis for the universities 
    in the data set
    '''
    keep = ['Private For-Profit', 'Private Nonprofit', 'Public']
    df = df[df['Type'].isin(keep)]
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Type', y='Earnings', data=df)
    plt.title('Graduate Earnings by Type of Institution')
    plt.xlabel('Type of Institution')
    plt.ylabel('Earnings ($)')


def main():

    print("rows: ", rows(df))
    print("missing: ", df.isnull().sum())
    print("Graduate Rate stats: ", graduate_rate_stats(df))
    print("Location stats: ", location_stats(df))
    print("Type stats: ", type_stats(df))
    print("Group stats: ", group_stats(df))
    print("Earnings stats: ", earnings_stats(df))
    graduate_rate_earnings_graph(df)
    plt.show()
    type_earnings_graph(df)
    plt.show()


if __name__ == "__main__":
    main()
