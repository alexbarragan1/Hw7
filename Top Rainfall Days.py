import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0
top_10_indices = np.argsort(rainfall)[-10:][::-1]

top_10_rainfall = rainfall[top_10_indices]

print("Top 10 Wettest Days:")
for i, idx in enumerate(top_10_indices):
    print(f"Day {idx + 1}: {top_10_rainfall[i]:.2f} mm")