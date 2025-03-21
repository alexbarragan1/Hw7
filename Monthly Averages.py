import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthly_rainfall = np.split(rainfall, np.cumsum(days_in_month))[:-1]
average_monthly_rainfall = [np.mean(month) for month in monthly_rainfall]

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("Average Monthly Rainfall:")
for month, avg_rainfall in zip(months, average_monthly_rainfall):
    print(f"{month}: {avg_rainfall:.2f} mm")