import matplotlib.pyplot as plt
import numpy as np

def graph_from_slope_intercept(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals

    return x_vals, y_vals