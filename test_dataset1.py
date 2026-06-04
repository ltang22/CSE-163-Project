'''
Lily Tang
CSE 163 AJ
This program tests the functions in dataset1.py with a small test DataFrame.
It includes tests for the row, missing values, graduate rate statistics,
location statistics, type statistics, group statistics, and earnings statistics
functions.
'''

import pandas as pd
from dataset1 import (
    rows,
    missing_values_and_columns,
    graduate_rate_stats,
    location_stats,
    type_stats,
    group_stats,
    earnings_stats,
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


def test_rows() -> None:
    '''
    Tests that the rows function correctly returns the
    correct number of rows in the test DataFrame.
    '''
    data = create_test_df()
    assert rows(data) == 3


def test_missing_values_and_columns() -> None:
    '''
    Tests that the missing_values_and_columns function correctly returns the
    correct number of missing values in each column of the test DataFrame.
    '''
    data = create_test_df()
    assert missing_values_and_columns(data).equals(pd.Series({'Name': 0,
                                                              'Years': 0,
                                                              'Location': 0,
                                                              'Type': 0,
                                                              'Place': 0,
                                                              'Group': 0,
                                                              'Graduate Rate':
                                                              0,
                                                              'Annual Cost': 0,
                                                              'Earnings': 0}))


def test_graduate_rate_stats() -> None:
    '''
    Tests that the graduate_rate_stats function correctly returns the
    correct statistics on the graduate rates in the test DataFrame.
    '''
    data = create_test_df()
    assert graduate_rate_stats(data).equals(pd.Series({'count': 3.0,
                                                       'mean': 90.0,
                                                       'std': 5.0,
                                                       'min': 85.0,
                                                       '25%': 87.5,
                                                       '50%': 90.0,
                                                       '75%': 92.5,
                                                       'max': 95.0}))


def test_location_stats() -> None:
    '''
    Tests that the location_stats function correctly returns the
    correct statistics on the locations in the test DataFrame.
    '''
    data = create_test_df()
    assert location_stats(data).equals(pd.Series({'count': 3, 'unique': 2,
                                                  'top':
                                                  'Cambridge, MA',
                                                  'freq': 2}))


def test_type_stats() -> None:
    '''
    Tests that the type_stats function correctly returns the
    correct statistics on the types in the test DataFrame.
    '''
    data = create_test_df()
    assert type_stats(data).equals(pd.Series({'count': 3, 'unique': 3, 'top':
                                              'Private Nonprofit', 'freq': 1}))


def test_group_stats() -> None:
    '''
    Tests that the group_stats function correctly returns the
    correct statistics on the groups in the test DataFrame.
    '''
    data = create_test_df()
    assert group_stats(data).equals(pd.Series({'count': 3, 'unique': 3,
                                               'top': 'Large', 'freq': 1}))


def test_earnings_stats() -> None:
    '''
    Tests that the earnings_stats function correctly returns the
    correct statistics on the earnings in the test DataFrame.
    '''
    data = create_test_df()
    assert earnings_stats(data).equals(pd.Series({'count': 3.0,
                                                  'mean': 110000.0,
                                                  'std': 10000.0,
                                                  'min': 100000.0,
                                                  '25%': 105000.0,
                                                  '50%': 110000.0,
                                                  '75%': 115000.0,
                                                  'max': 120000.0}))


def main():
    '''
    Runs all the test functions to ensure that the functions in data2.py
    are working correctly.
    '''
    test_rows()
    test_missing_values_and_columns()
    test_graduate_rate_stats()
    test_location_stats()
    test_type_stats()
    test_group_stats()
    test_earnings_stats()


if __name__ == '__main__':
    main()
