"""
This module contains the function calc_cost that calculates
the cost (error) of a linear regression model.
"""


def calc_cost(data, theta0, theta1):
    """
    Cost function for linear regression.

    Parameters:
    -----------
    data : pandas.DataFrame
        The dataset containing 'km' (features) and 'price' (targets).
    theta0 : float
        Model parameter theta0 (intercept).
    theta1 : float
        Model parameter theta1 (slope).

    Returns:
    --------
    None
    """
    m = len(data)
    total_cost = 0
    for i in range(m):
        prediction = theta0 + theta1 * data['km'][i]
        error = (prediction - data['price'][i]) ** 2
        total_cost += error
    print(total_cost / (2 * m))
