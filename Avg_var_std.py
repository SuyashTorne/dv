# 1.Calculate the average, variance and standard deviation in Python using NumPy

import numpy as np
import pandas as pd
df = pd.DataFrame({'numbers':[2,4,5,56,6,7,7,7,10,34,4,34,3,2,1,1,1,34,5,5,6,6,3]})
average = np.mean(df['numbers'])
variance = np.var(df['numbers'])
std_deviation = np.std(df['numbers'])
print("Average:",average,"\n" "Variance:",variance, "\n"  "std_deviation:", std_deviation)
