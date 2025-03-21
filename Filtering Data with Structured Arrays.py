import numpy as np

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

rainy_days_mask = structured_array['is_rainy']
rainy_days = structured_array[rainy_days_mask]
average_rainfall_rainy_days = np.mean(rainy_days['rainfall'])

print("Rainy Days:")
print(rainy_days)
print(f"\nAverage Rainfall on Rainy Days: {average_rainfall_rainy_days:.2f} mm")