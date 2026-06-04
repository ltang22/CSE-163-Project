"""
Natalie Olson
CSE 163 AJ
This program analyzes a dataset of educational institutions in the United
States. It includes functions to find missing values, calculating medians,
producing a five number summary, and creating two visualizations based on
chosen columns of the dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt


def missing(df: pd.DataFrame) -> None:
    """
    This function takes in a pandas dataframe of educational institution data
    and prints out the number of missing values in each column of the dataset.
    """
    print(df.isnull().sum())


def median(numbers: list[int]) -> float:
    """
    Given a sorted list of numbers, returns the median.
    """
    n = len(numbers)

    result = None
    if n % 2 != 0:
        result = numbers[n // 2]
    else:
        upper_num = numbers[n // 2]
        lower_num = numbers[n // 2 - 1]
        result = (upper_num + lower_num) / 2

    return result


def five_number_summary(df: pd.DataFrame) -> None:
    """
    Given a pandas dataframe of educational institution data, prints a tuple
    of the five-number summary (minimum, first quartile, median, third
    quartile, and maximum) for each numeric column in the dataframe.
    """
    columns = list(df.columns)
    for col in columns:
        if df[col].dtype == int or df[col].dtype == float:
            col_vals = list(df[col])
            col_vals = sorted(col_vals)
            n = len(col_vals)
            if n % 2 == 0:
                lower_half = col_vals[:n // 2]
                upper_half = col_vals[n // 2:]
            else:
                lower_half = col_vals[:n // 2]
                upper_half = col_vals[n // 2 + 1:]
            med = median(col_vals)
            lower_med = median(lower_half)
            upper_med = median(upper_half)
            print(str(col), (col_vals[0], lower_med, med, upper_med,
                             col_vals[-1]))


def mean_and_std(df: pd.DataFrame) -> None:
    """
    This function takes in a pandas dataframe of education institution data
    and finds the mean and standard deviation for the numeric columns of the
    dataset, rounds to two decimal places, then prints them out.
    """
    columns = list(df.columns)   
    for col in columns:
        if df[col].dtype == int or df[col].dtype == float:
            mean = df[col].mean()
            std = df[col].std()
            print(str(col), round(mean, 2), round(std, 2))


def endow_grad_viz(df: pd.DataFrame) -> None:
    """
    This function takes in the institutional education dataset and creates a
    scatterplot that compares the endowment percentile to the number of
    graduates who graduated within the normal time frame.
    """
    plt.figure(figsize=(12, 9))
    plt.scatter(x=df["endow_percentile"], y=df["grad_100_value"],
                color="black")
    plt.legend = True
    plt.title("Normal Graduation Timeline Compared to Endowment Percentile")
    plt.xlabel("Number of Graduates")
    plt.ylabel("Endowment Percentile")
    plt.show()


def fac_award_viz(df: pd.DataFrame) -> None:
    """
    This function takes in the institutional education dataset and creates a
    histogram to compare the full-time faculty percentile to the awards-per-
    100-undergraduate students number.
    """
    fac_and_awards = df[["ft_fac_percentile", "awards_per_value"]]
    plt.hist(fac_and_awards, bins=20)
    plt.legend = True
    plt.title("Full-Time Faculty Percentile vs. Number of "
              "Awards per 100 Undergrads")
    plt.xlabel("Full-Time Faculty")
    plt.ylabel("Awards Value")
    plt.show()


def main():
    institutions = pd.read_csv("cc_institution_details.csv")
    print(len(institutions))
    new_df = institutions[["awards_per_value", "exp_award_value",
                           "exp_award_percentile", "grad_100_value",
                           "ft_fac_percentile", "aid_percentile",
                           "endow_percentile", "pell_percentile", "control",
                           "med_sat_percentile"]]
    public_count = (new_df["control"] == "Public").sum()
    print(public_count)
    priv_n_p_count = (new_df["control"] == "Private not-for-profit").sum()
    print(priv_n_p_count)
    priv_f_p_count = (new_df["control"] == "Private for-profit").sum()
    print(priv_f_p_count)
    five_number_summary(new_df)
    missing(new_df)
    mean_and_std(new_df)
    endow_grad_viz(new_df)
    fac_award_viz(new_df)


if __name__ == '__main__':
    main()
