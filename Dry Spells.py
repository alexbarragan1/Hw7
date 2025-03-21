import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0

dry_days = rainfall == 0
max_length = 0
current_length = 0

for day in dry_days:
    if day:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0

print(f"Longest consecutive dry spell: {max_length} days")