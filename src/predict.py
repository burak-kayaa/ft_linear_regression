"""
This module contains the main function to predict
the price of a car given its milage.
"""
from src.constants import DATA_FILE_PATH, THS_FILE_PATH
from src.utils.load import load_data
from src.utils.normalize import denormalize_value, normalize_value
from src.utils.get_input import get_milage
from src.utils.theta import get_thetas


def estimate_price(theta0, theta1, milage, data):
    """
    Estimate the price of a car given its milage

    Parameters
    ----------
    theta0 : float
        The intercept of the linear regression model
    theta1 : float
        The slope of the linear regression model
    milage : float
        The milage of the car
    data : dict
        A dictionary containing the 'km' and 'price' columns of the dataset

    Returns
    -------
    None
    """
    normalized_milage = normalize_value(milage, data['km'])
    price = theta0 + theta1 * normalized_milage
    denormalized_price = denormalize_value(price, data['price'])
    print(f"The estimated price is: {denormalized_price}")


def main():
    """
    Main function to predict the price of a car given its milage
    """
    data = load_data(DATA_FILE_PATH)
    if data is None:
        return
    theta0, theta1 = get_thetas(THS_FILE_PATH)
    milage = get_milage()
    estimate_price(theta0, theta1, milage, data)


if __name__ == '__main__':
    main()
