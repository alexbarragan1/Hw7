import numpy as np

random_numbers = np.random.randint(1, 1000, size=100)
mask = random_numbers % 3 == 0
random_numbers[mask] = -1
print(random_numbers)