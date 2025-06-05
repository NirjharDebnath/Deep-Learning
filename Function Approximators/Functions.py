import numpy as np 
import matplotlib.pyplot as plt 
import math

# Polynomial
def polynomial(x):
    return x**3 + 2*x**2 - x + 1

def sinusoidal(x):
    return np.sin(x)

def exponential(x):
    return np.exp(x)

def peicewisefn(x):
    y = np.array([10 * np.cos(x) if x>0 else x**2 for x in x])
    return y

def absolute(x):
    return np.abs(x)

def composite(x):
    return np.sin(x**2) + np.exp(-np.abs(x))


plt.style.use("seaborn-v0_8-whitegrid")
plt.plot(np.linspace(-10, 10, 1000), composite(np.linspace(-10, 10, 1000)))
plt.axhline(y=0, color='black', linewidth=1)  # X-axis line
plt.axvline(x=0, color='black', linewidth=1)  # Y-axis line
plt.title("Exponential", fontsize=16, weight="bold")
plt.xlabel("X axis", fontsize=12, weight="bold")
plt.ylabel("Y axis", fontsize=12, weight="bold")
plt.legend()
plt.grid(linestyle="--", alpha=0.8)
plt.show()