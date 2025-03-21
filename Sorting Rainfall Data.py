import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0
sorted_rainfall = np.sort(rainfall)
median_rainfall = np.median(sorted_rainfall)

print("Sorted Rainfall (ascending order):")
print(sorted_rainfall)

print(f"\nMedian Rainfall: {median_rainfall:.2f} mm")