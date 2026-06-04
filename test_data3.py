'''
Lily Tang, Natalie Olson, Amuktha Josyula
CSE 163 AJ
This program tests the functions a given datasetwith a small test DataFrame.
It includes tests for the row, missing values, graduate rate statistics,
location statistics, type statistics, group statistics, and earnings statistics
functions.
'''

import pandas as pd
from dataset3 import (
    missing,
    median,
    five_number_summary,
    mean_and_std,
)


def create_test_df() -> pd.DataFrame:
    '''
    Creates a small test DataFrame with similar university data to the
    original dataset for testing purposes.
    '''
    return pd.DataFrame({'Name': ['MIT', 'Stanford', 'Harvard'],
                        'Years': [4, 4, 4],
                         'Location': ['Cambridge, MA', 'Stanford, CA',
                                      'Cambridge, MA'],
                         'Type': ['Private Nonprofit', 'Public',
                                  'Private For-Profit'],
                         'Place': ['City', 'Suburban', 'Town'],
                         'Group': ['Large', 'Medium', 'Small'],
                         'Graduate Rate': ['95%', '90%', '85%'],
                         'Annual Cost': ['$50k', '$60k', '$70k'],
                         'Earnings': ['$120k', '$110k', '$100k']})


def test_missing() -> None:
    '''
    Tests that the missing function correctly returns the
    correct number of missing values in the test DataFrame.
    '''
    data = create_test_df()
    assert missing(data) == 0


def test_median() -> None:
    '''
    Tests that the median function correctly returns the
    correct median of a list of numbers.
    '''
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5


def test_five_number_summary() -> None:
    '''
    Tests that the five_number_summary function correctly returns the
    correct five number summary for each numeric column in the test DataFrame.
    '''
    data = create_test_df()
    assert five_number_summary(data) == {'Years': (4, 4, 4, 4, 4),
                                         'Graduate Rate': (85.0, 87.5, 90.0,
                                                           92.5, 95.0),
                                         'Annual Cost': (50000.0, 55000.0,
                                                         60000.0, 65000.0,
                                                         70000.0),
                                         'Earnings': (100000.0, 105000.0,
                                                      110000.0, 115000.0,
                                                      120000.0)}


def test_mean_and_std() -> None:
    '''
    Tests that the mean_and_std function correctly returns the
    correct mean and standard deviation for each numeric column in the test
    DataFrame.
    '''
    data = create_test_df()
    assert mean_and_std(data) == {'Years': (4.0, 0.0),
                                  'Graduate Rate': (90.0, 5.0),
                                  'Annual Cost': (60000.0, 10000.0),
                                  'Earnings': (110000.0, 10000.0)}


def main():
    '''
    Runs all the test functions to ensure that the functions in data2.py
    are working correctly.
    '''
    test_missing()
    test_median()
    test_five_number_summary()
    test_mean_and_std()


if __name__ == '__main__':
    main()
