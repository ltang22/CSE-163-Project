"""Tests for dataset3.py."""

import io
from contextlib import redirect_stdout
from unittest.mock import patch

import matplotlib
import pandas as pd

matplotlib.use("Agg")

import dataset3


def test_median_odd() -> None:
    assert dataset3.median([1, 3, 5]) == 3


def test_median_even() -> None:
    assert dataset3.median([1, 2, 3, 4]) == 2.5


def test_missing_prints_counts() -> None:
    df = pd.DataFrame({"a": [1, pd.NA], "b": [pd.NA, 2]})
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        dataset3.missing(df)
    output = buffer.getvalue()

    assert "a" in output
    assert "b" in output
    assert "1" in output


def test_five_number_summary_prints() -> None:
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [10, 20, 30, 40], "z": ["a", "b", "a", "b"]})
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        dataset3.five_number_summary(df)
    output = buffer.getvalue()

    assert "x" in output
    assert "(1, 1.5, 2.5, 3.5, 4)" in output
    assert "y" in output
    assert "(10, 17.5, 25.0, 32.5, 40)" in output


def test_mean_and_std_prints() -> None:
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [10, 20, 30, 40], "z": ["a", "b", "a", "b"]})
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        dataset3.mean_and_std(df)
    output = buffer.getvalue()

    assert "x" in output
    assert "2.5" in output
    assert "y" in output
    assert "25.0" in output


@patch("dataset3.plt.show")
def test_endow_grad_viz_no_error(mock_show) -> None:
    df = pd.DataFrame({"endow_percentile": [10, 20, 30], "grad_100_value": [100, 200, 300]})
    dataset3.endow_grad_viz(df)
    mock_show.assert_called_once()


@patch("dataset3.plt.show")
def test_fac_award_viz_no_error(mock_show) -> None:
    df = pd.DataFrame(
        {
            "ft_fac_percentile": [5, 15, 25],
            "awards_per_value": [1, 2, 3],
        }
    )
    dataset3.fac_award_viz(df)
    mock_show.assert_called_once()


if __name__ == "__main__":
    test_median_odd()
    test_median_even()
    test_missing_prints_counts()
    test_five_number_summary_prints()
    test_mean_and_std_prints()
    test_endow_grad_viz_no_error()
    test_fac_award_viz_no_error()
    print("All dataset3 tests passed.")
