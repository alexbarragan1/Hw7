import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0
percentile_90 = np.percentile(rainfall, 90)

print(f"90th Percentile of Rainfall: {percentile_90:.2f} mm")