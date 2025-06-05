import numpy as np 
import matplotlib.pyplot as plt 

def data_uniform(low=-10, high=10,size=1000):
    return np.random.uniform(low, high, size)

def data_normal(mean=0, std=2, size=1000):
    return np.random.normal(mean, std, size)

def data_line(low=-10, high=10, size=1000):
    return np.linspace(low, high, size)

x, y = data_line(), data_line()
plt.style.use("seaborn-v0_8-whitegrid")
plt.scatter(x, y, c=x, cmap="Blues", alpha=0.8)
plt.axhline(y=0, color='black', linewidth=1)  # X-axis line
plt.axvline(x=0, color='black', linewidth=1)  # Y-axis line
plt.title("Exponential", fontsize=16, weight="bold")
plt.xlabel("X axis", fontsize=12, weight="bold")
plt.ylabel("Y axis", fontsize=12, weight="bold")
plt.legend()
plt.grid(linestyle="--", alpha=0.8)
plt.show()