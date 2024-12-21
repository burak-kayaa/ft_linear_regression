"""
Plotting module
"""
import matplotlib.pyplot as plt


def plot_data(data, theta0, theta1):
    """
    Plot data
    """
    plt.scatter(data['km'], data['price'], color='blue')
    plt.plot(data['km'], theta0 + theta1 * data['km'], color='red')
    plt.title('Price vs Mileage')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.show()
