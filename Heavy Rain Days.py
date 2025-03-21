import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0
heavy_rain_mask = rainfall > 5
num_heavy_rain_days = np.sum(heavy_rain_mask)
percentage_heavy_rain = (num_heavy_rain_days / 365) * 100
print(f"Percentage of days with rainfall > 5 mm: {percentage_heavy_rain:.2f}%")