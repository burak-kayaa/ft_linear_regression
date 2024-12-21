"""
This module contains a function to load a CSV file into a pandas DataFrame.
"""
import pandas as pd


def load_data(file_path):
    """
    Load a CSV file into a pandas DataFrame

    Parameters
    ----------
    file_path : str
        The path to the CSV file to load

    Returns
    -------
    pandas.DataFrame
        The loaded DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
