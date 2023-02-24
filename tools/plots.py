import matplotlib.pyplot as plt
import sys
import math
import numpy as np
from tools import sieve

def simple_plot(all_nmax = np.arange(100, 5000, 100)):
    plt.plot(all_nmax, sieve.proportion_prints(all_nmax))
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    
def log_plot(all_nmax = np.arange(100, 5000, 100)):
    plt.plot(all_nmax, sieve.proportion_prints(all_nmax))
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    plt.xscale("log")
    plt.yscale("log")
    
def plot_sieve(all_nmax = np.arange(100, 5000, 100), log_scale = True):
    if log_scale:
        return log_plot(all_nmax)
    else:
        return simple_plot(all_nmax)
    import matplotlib.pyplot as plt
