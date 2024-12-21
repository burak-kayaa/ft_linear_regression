"""
This module contains functions to get, update and save
the values of theta0 and theta1
"""
import sys

from src.constants import THS_FILE_PATH


def get_thetas(file_path):
    """
    Get the theta0 and theta1 values from a file

    Parameters
    ----------
    file_path : str
        The path to the file containing the theta0 and theta1 values

    Returns
    -------
    float
        The theta0 value
    float
        The theta1 value
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            line = f.readline()
            theta0, theta1 = line.split()
            return float(theta0), float(theta1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def update_theta(data, theta0, theta1, learning_rate):
    """
    Update the values of theta0 and theta1 using the gradient descent algorithm

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data
    theta0 : float
        The current value of theta0
    theta1 : float
        The current value of theta1
    learning_rate : float
        The learning rate of the algorithm

    Returns
    -------
    float
        The updated value of theta0
    float
        The updated value of theta1
    """
    sum_theta0 = 0
    sum_theta1 = 0
    for _, rw in data.iterrows():
        sum_theta0 += (theta0 + theta1 * rw['km']) - rw['price']
        sum_theta1 += ((theta0 + theta1 * rw['km']) - rw['price']) * rw['km']
    new_theta0 = theta0 - learning_rate * (1 / len(data)) * sum_theta0
    new_theta1 = theta1 - learning_rate * (1 / len(data)) * sum_theta1
    return new_theta0, new_theta1


def save_theta(theta0, theta1):
    """
    Save the values of theta0 and theta1 in a file

    Parameters
    ----------
    theta0 : float
        The value of theta0 to save
    theta1 : float
        The value of theta1 to save
    """
    with open(THS_FILE_PATH, 'w', encoding="utf-8") as f:
        f.write(f"{theta0} {theta1}")
