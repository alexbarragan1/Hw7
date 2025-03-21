import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0
rainy_days_mask = rainfall > 0
num_rainy_days = np.sum(rainy_days_mask)
print(f"Number of rainy days: {num_rainy_days}")