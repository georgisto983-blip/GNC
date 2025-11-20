import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *

class Ploter():

    def __init__(self):
        pass

    @staticmethod
    def plot_data_and_fit(x, x_err, y, y_err, linear_func, out, T_for_plot):
        
        x_fit = np.linspace(x[0], x[-1], 1000)
        y_fit = linear_func(out.beta, x_fit)
        plt.errorbar(x, y, xerr=x_err, yerr=y_err, linestyle='None', marker='x', capsize=10, label='Data with error bars', color='red', alpha=0.5)
        plt.plot(x_fit, y_fit, color='blue')
        plt.scatter(x, y, color='red')
        plt.xlabel("Plunger Distance, $\mu$m")
        plt.ylabel(r"$ln\frac{Unshifted}{Unshifted + Shifted}$")
        plt.title("Linear Fit to Determine Half-Life\n")
        plt.xticks(np.arange(min(x), max(x)+1, 0.5))
        #plt.yticks(np.arange(min(y)-0.1, max(y)+0.2, 0.2))
        plt.text(0.05, 0.95, r'$T_{1/2}$ ' + f"{T_for_plot}", transform=plt.gca().transAxes, verticalalignment='top')
        # plt.subplots_adjust(bottom = -0.05)
        # plt.subplots_adjust(left = -0.05)
        plt.grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.5, color='blue')
        plt.show()       