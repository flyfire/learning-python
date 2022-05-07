import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    mu, sigma = 2, 0.5
    v = np.random.normal(mu, sigma, 10000)
    plt.hist(v, bins=50, density=1)
    plt.show()
    (n, bins) = np.histogram(v, bins=50, density=True)
    plt.plot(.5*(bins[1:]+bins[:-1]), n)
    plt.show()