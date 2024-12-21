"""
This module contains functions to get input from the user
"""


def get_milage():
    """
    Get the milage of the car from the user

    Returns
    -------
    float
        The milage of the car
    """
    while True:
        try:
            milage = float(input("Enter the milage of the car: "))
            if milage < 0:
                raise ValueError
            return milage
        except ValueError:
            print("Please enter a positive number")
