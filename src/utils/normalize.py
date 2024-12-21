"""
This module contains functions to normalize and denormalize columns and values
"""


def normalize_column(data, column_name):
    """
    Normalize a column of a DataFrame

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the column to normalize
    column_name : str
        The name of the column to normalize

    Returns
    -------
    pandas.Series
        The normalized column
    """
    col_min = data[column_name].min()
    col_max = data[column_name].max()
    return (data[column_name] - col_min) / (col_max - col_min)


def denormalize_column(data, column_name):
    """
    Denormalize a column of a DataFrame

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the column to denormalize
    column_name : str
        The name of the column to denormalize

    Returns
    -------
    pandas.Series
        The denormalized column
    """
    col_min = data[column_name].min()
    col_max = data[column_name].max()
    return data[column_name] * (col_max - col_min) + col_min


def normalize_value(value, data):
    """
    Normalize a value using the min and max values of a column

    Parameters
    ----------
    value : float
        The value to normalize
    data : pandas.Series
        The column used to normalize the value

    Returns
    -------
    float
        The normalized value
    """
    col_min = data.min()
    col_max = data.max()
    return (value - col_min) / (col_max - col_min)


def denormalize_value(value, data):
    """
    Denormalize a value using the min and max values of a column

    Parameters
    ----------
    value : float
        The value to denormalize
    data : pandas.Series
        The column used to denormalize the value

    Returns
    -------
    float
        The denormalized value
    """
    col_min = data.min()
    col_max = data.max()
    return value * (col_max - col_min) + col_min
