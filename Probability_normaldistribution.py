# 2.How to calculate probability in a normal distribution given mean and standard deviation in Python?

from scipy.stats import norm
import numpy as np
data_start = -5
data_end = 5
data_points = 11
data = np.linspace(data_start, data_end, data_points) 
mean = np.mean(data)
std = np.std(data)
probability_pdf = norm.pdf(3, loc=mean, scale=std)
print(probability_pdf)
