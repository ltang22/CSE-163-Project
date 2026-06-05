
"""
Amuktha Josyula, Natalie Olson, Lily Tang
CSE 163
This file filters and creates visualizations
from the University database from the US DOE.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool


def statistics(variable: str, data: pd.DataFrame) -> str:
    """
    This function retrieves a set of sample statistics for the given dataset
    variable.
    """
    return data[variable].describe()


def rows(data: pd.DataFrame) -> int:
    '''
    Takes in the dataframe with the dataset and returns the
    number of rows in the dataframe.
    '''
    return len(data)


def missing_values_and_columns(data: pd.DataFrame) -> pd.Series:
    '''
    Takes in the data frame with the dataset and returns
    a series of the number of missing values in each
    column of the dataframe.
    '''
    return data.isnull().sum()


def visualization_one(data: pd.DataFrame, var1: str, var2: str, var1_name: str,
                      var2_name: str, title: str) -> None:
    """
    This function creates a scatterplot for the given variables.
    """
    graph_one = sns.relplot(data=data, x=var1, y=var2)
    graph_one.set_axis_labels(var1_name, var2_name)
    graph_one.fig.suptitle(title, y=1.02)


def visualization_two(data: pd.DataFrame, var1: str, var2: str, var1_name: str,
                      var2_name: str, title: str) -> None:
    """
    This function creates a bar graph for the given variables.
    """
    graph_two = sns.catplot(data=data, x=var1, y=var2, kind='bar',
                            hue=var1)
    graph_two.set_axis_labels(var1_name, var2_name)
    graph_two.fig.suptitle(title, y=1.02)


def interactive_visualization(x: str, y: str, data: pd.DataFrame):
    """
    This function creates an interactive scatterplot for the given variables.
    In this case the variables are admission rate and median earnings 6 years
    after graduation.
    """
    source = ColumnDataSource(data)
    graph = figure(title="Interactive Visualization of Admission "
                   "Rate and Salary", x_axis_label="Admission Rate",
                   y_axis_label="Median Earnings 6 years after graduation",
                   tools="pan, wheel_zoom, box_zoom, reset",
                   x_range=(0, 1))
    graph.scatter(x=x, y=y, source=source, size=8)
    hover = HoverTool(tooltips=[
        ("University", "@INSTNM"),
        (x, f"@{x}"),
        (y, f"@{y}")
    ])
    graph.add_tools(hover)
    show(graph)


def main():

    # Processing and filtering the dataset
    data = pd.read_csv('Cohorts dataset CSV.csv', low_memory=False)
    filtered_data = data[['INSTNM', 'ADM_RATE', 'SAT_AVG', 'MD_EARN_WNE_P6',
                          'PCIP11', 'PCIP52', 'PCIP14', 'MEDIAN_HH_INC',
                          'HIGHDEG']]
    filtered_data.to_csv('new.csv', index=False)

    # Classify each number with it's actual degree
    filtered_data["HIGHDEG"] = filtered_data["HIGHDEG"].map({0:
                                                             "Non-degree-"
                                                             "granting "
                                                             "institution",
                                                             1: "Certificate "
                                                             "below associate"
                                                             " degree", 2:
                                                             "Associate "
                                                             "degree", 3:
                                                             "Bachelor’s "
                                                             "degree", 4:
                                                             "Graduate degree"
                                                             " (Master’s or "
                                                             "higher)"})

    # Basic information about the dataset
    print("Rows:" + str(rows(filtered_data)))
    print(missing_values_and_columns(filtered_data))

    # Key statistics for all the dataset variables
    print(statistics("ADM_RATE", filtered_data))
    print(statistics("SAT_AVG", filtered_data))
    print(statistics("MD_EARN_WNE_P6", filtered_data))
    print(statistics("PCIP11", filtered_data))
    print(statistics("PCIP52", filtered_data))
    print(statistics("PCIP14", filtered_data))

    # Visualization 1: Scatterplot
    visualization_one(filtered_data, "ADM_RATE", "SAT_AVG",
                      "Admission Rate (proportion)", "Average SAT",
                      "Average SAT score by Admission rate")

    # Visualization 2: Bar graph
    visualization_two(filtered_data, "HIGHDEG", "MD_EARN_WNE_P6",
                      "Highest Degree Offered", "Median Earnings 6 Years "
                      "Post Graduation", "Highest Degree vs. Median Earnings")

    # Visualization 3: Interactive Scatterplot
    interactive_visualization("ADM_RATE", "MD_EARN_WNE_P6", filtered_data)
    plt.show()


if __name__ == '__main__':
    main()
