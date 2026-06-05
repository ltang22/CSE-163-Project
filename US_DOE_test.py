'''
Amuktha Josyula
CSE 163
This program tests the functions in US_DOE_analysis with a small test
DataFrame. It includes tests for the row, missing values, and different
statistics for the columns in the second dataset.
'''

import pandas as pd
from US_DOE_analysis import (
    rows,
    missing_values_and_columns,
    statistics
)


def create_test_df() -> pd.DataFrame:
    '''
    Creates a small test DataFrame with similar university data to the
    original dataset for testing purposes.
    '''
    return pd.DataFrame({'INSTNM': ['MIT', 'Stanford', 'Harvard'],
                        'ADM_RATE': [1, 2, 3],
                         'SAT_AVG': [1400, 1500, 1600],
                         'MD_EARN_WNE_P6': [100000, 200000, 300000],
                         'PCIP11': [0.5, 0.6, 0.7],
                         'PCIP52': [0.5, 0.6, 0.7],
                         'PCIP14': [0.4, 0.5, 0.6],
                         'MEDIAN_HH_INC': [60000, 70000, 80000],
                         'HIGHDEG': [4, 4, 4]})


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
    assert missing_values_and_columns(data).equals(pd.Series({'INSTNM': 0,
                                                              'ADM_RATE': 0,
                                                              'SAT_AVG': 0,
                                                              'MD_EARN_WNE_'
                                                              'P6': 0,
                                                              'PCIP11': 0,
                                                              'PCIP52': 0,
                                                              'PCIP14': 0,
                                                              'MEDIAN_HH_'
                                                              'INC': 0,
                                                              'HIGHDEG': 0}))


def test_statistics() -> None:
    '''
    Tests that the graduate_rate_stats function correctly returns the
    correct statistics on the graduate rates in the test DataFrame.
    '''
    data = create_test_df()

    assert statistics('ADM_RATE', data).equals(pd.Series({'count': 3.0,
                                                          'mean': 2.0,
                                                          'std': 1.0,
                                                          'min': 1.0,
                                                          '25%': 1.5,
                                                          '50%': 2.0,
                                                          '75%': 2.5,
                                                          'max': 3.0}))
    assert statistics('SAT_AVG', data).equals(pd.Series({'count': 3.0,
                                                         'mean': 1500.0,
                                                         'std': 100.0,
                                                         'min': 1400.0,
                                                         '25%': 1450.0,
                                                         '50%': 1500.0,
                                                         '75%': 1550.0,
                                                         'max': 1600}))
    assert statistics('MD_EARN_WNE_P6', data).equals(pd.Series({'count': 3.0,
                                                                'mean':
                                                                200000.0,
                                                                'std':
                                                                100000.0,
                                                                'min':
                                                                100000.0,
                                                                '25%':
                                                                150000.0,
                                                                '50%':
                                                                200000.0,
                                                                '75%':
                                                                250000.0,
                                                                'max':
                                                                300000.0}))

    assert statistics('MEDIAN_HH_INC', data).equals(pd.Series({'count': 3.0,
                                                               'mean': 70000.0,
                                                               'std': 10000.0,
                                                               'min': 60000.0,
                                                               '25%': 65000.0,
                                                               '50%': 70000.0,
                                                               '75%': 75000.0,
                                                               'max':
                                                               80000.0}))
    assert statistics('HIGHDEG', data).equals(pd.Series({'count': 3.0,
                                                         'mean': 4,
                                                         'std': 0,
                                                         'min': 4,
                                                         '25%': 4,
                                                         '50%': 4,
                                                         '75%': 4,
                                                         'max': 4}))


def main():
    '''
    Runs all the test functions to ensure that the functions in data2.py
    are working correctly.
    '''
    test_rows()
    test_missing_values_and_columns()
    test_statistics()


if __name__ == '__main__':
    main()
