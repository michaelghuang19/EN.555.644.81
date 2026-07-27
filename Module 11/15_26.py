import numpy as np

weekly_returns = np.array([30.2, 32.0, 31.1, 30.1, 30.2, 30.3, 30.6, 33.0, 32.9, 33.0, 33.5, 33.5, 33.7, 33.5, 33.2])

u = np.log(weekly_returns[1:] / weekly_returns[:-1])
sum_u = np.sum(u)
sum_u_squared = np.sum(u**2)

weekly_returns_sd = np.sqrt((sum_u_squared - (sum_u**2) / len(weekly_returns)) / (len(weekly_returns) - 1))

annual_vol = weekly_returns_sd * np.sqrt(52)

vol_standard_error = annual_vol / np.sqrt(2 * len(weekly_returns))

print(f"Weekly returns SD: {weekly_returns_sd}")
print(f"Annual volatility estimate: {annual_vol}")
print(f"Standard error of estimate: {vol_standard_error}")
