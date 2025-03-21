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

structured_array['day'] = np.arange(1, 366)  # Days from 1 to 365
structured_array['rainfall'] = rainfall      # Rainfall data
structured_array['is_rainy'] = rainfall > 0  # Boolean mask for rainy days

print("Structured Array:")
print(structured_array)