import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)
	intermediate = (X.T @ X)
	w = np.linalg.inv(intermediate) @ X.T @ y
	return w