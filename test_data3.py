'''
Lily Tang, Natalie Olson, Amuktha Josyula
CSE 163 AJ
This program tests the functions a given datasetwith a small test DataFrame.
It includes tests for the missing values and median functions.
'''

import pandas as pd
from dataset3 import (
    missing,
    median,
)


def create_test_df() -> pd.DataFrame:
    '''
    Creates a small test DataFrame with similar university data to the
    original dataset for testing purposes.
    '''
    return pd.DataFrame({'awards_per_value': [10, 15, 5],
                        'exp_award_value': [11111, 2342, 44980],
                         'exp_award_percentile': [80, 40, 20],
                         'grad_100_value': [10, 11, 12],
                         'ft_fac_percentile': [90, 30, 55],
                         'aid_percentile': [90, 95, 80],
                         'endow_percentile': [30, 33, 37],
                         'pell_percentile': [70, 17, 81],
                         'med_sat_percentile': [50, 87, 100]})


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


def main():
    '''
    Runs all the test functions to ensure that the functions in data3.py
    are working correctly.
    '''
    test_missing()
    test_median()


if __name__ == '__main__':
    main()
