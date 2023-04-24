import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Generate some random time-series data
np.random.seed(0)
n_samples = 100
data = np.random.randn(n_samples)

# Fit the ARIMA model
model = ARIMA(data, order=(1, 1, 1))
results = model.fit()

# Plot the data and the fitted values
fig, ax = plt.subplots()
ax.plot(data, label='Data')
ax.plot(results.fittedvalues, color='red', label='Fitted Values')
ax.legend()
plt.show()

# Predict future values
n_steps = 10
forecast = results.forecast(steps=n_steps)

# Plot the predicted values
fig, ax = plt.subplots()
ax.plot(data, label='Data')
ax.plot(np.arange(n_samples, n_samples+n_steps), forecast, color='red', label='Predicted Values')
ax.legend()
plt.show()
