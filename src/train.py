"""Train model module"""

from src.bonus.calc_cost import calc_cost
from src.bonus.plotting import plot_data
from src.utils.load import load_data
from src.utils.normalize import normalize_column
from src.constants import DATA_FILE_PATH
from src.utils.theta import save_theta, update_theta


def main(bonus=True):
    """
    Training model main function
    """
    data = load_data(DATA_FILE_PATH)
    if data is None:
        return
    data['km'] = normalize_column(data, 'km')
    data['price'] = normalize_column(data, 'price')
    theta0 = 0
    theta1 = 0
    learning_rate = 0.1
    nb_iterations = 1000
    for _ in range(nb_iterations):
        theta0, theta1 = update_theta(data, theta0, theta1, learning_rate)
    save_theta(theta0, theta1)
    if bonus:
        calc_cost(data, theta0, theta1)
        plot_data(data, theta0, theta1)


if __name__ == '__main__':
    main(bonus=False)
