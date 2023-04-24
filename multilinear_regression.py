import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(0)
n_samples = 10
X = np.random.randn(n_samples, 2)
y = 2 * X[:, 0] - 3 * X[:, 1] + np.random.randn(n_samples)

# Add a column of ones to X for the intercept term
X = np.hstack((np.ones((n_samples, 1)), X))

# Compute the coefficients using the normal equation
coeffs = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

# Print the coefficients and intercept
print("Coefficients:", coeffs[1:])
print("Intercept:", coeffs[0])

# Plot the data and the regression line
fig, ax = plt.subplots()
ax.scatter(X[:, 1], y, label='Data')
ax.plot(X[:, 1], X.dot(coeffs), color='red', label='Regression Line')
ax.legend()
plt.show()
