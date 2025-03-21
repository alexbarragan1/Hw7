import numpy as np  # Import NumPy

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0

dtype = [
    ('day', int),
    ('rainfall', float),
    ('is_rainy', bool)
]

structured_array = np.empty(365, dtype=dtype)
structured_array['day'] = np.arange(1, 366)
structured_array['rainfall'] = rainfall
structured_array['is_rainy'] = rainfall > 0

sorted_indices = np.argsort(structured_array['rainfall'])[::-1]
sorted_array = structured_array[sorted_indices]
top_5_rainiest_days = sorted_array[:5]

print("Top 5 Rainiest Days:")
for day in top_5_rainiest_days:
    print(f"Day {day['day']}: {day['rainfall']:.2f} mm")