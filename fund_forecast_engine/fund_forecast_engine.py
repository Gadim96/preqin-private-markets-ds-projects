import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load dataset
df = pd.read_csv("mock_fund_cashflows.csv")
df = df.sort_values("Year")
y = df["Distributions"]

# Fit SARIMA model
model = SARIMAX(y, order=(1, 1, 1), seasonal_order=(0, 1, 1, 4))
results = model.fit(disp=False)

# Forecast next 5 years
forecast = results.get_forecast(steps=5)
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# ---- IRR Curve Simulation ----
# Assumption: 10% annual IRR on a starting NAV base
initial_nav = df["NAV"].mean()  # You can choose a smarter base if needed
irr = 0.10
future_years = np.array(range(df["Year"].iloc[-1] + 1, df["Year"].iloc[-1] + 6))
n = len(future_years)

# IRR cumulative payout curve (simplified)
irr_curve = [initial_nav * ((1 + irr) ** i - 1) * 0.3 for i in range(1, n + 1)]

# ---- Plotting ----
plt.figure(figsize=(10, 6))

# Actual distributions
plt.plot(df["Year"], y, label="Observed Distributions", color="blue")

# SARIMA forecast
plt.plot(future_years, forecast_mean, label="SARIMA Forecast", linestyle="--", color="orange")
plt.fill_between(future_years, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color="gray", alpha=0.2)

# IRR curve
plt.plot(future_years, irr_curve, label="Simulated IRR Projection (10%)", linestyle=":", color="green")

# Styling
plt.xlabel("Year")
plt.ylabel("Distributions")
plt.title("Private Equity Fund Distribution Forecast: SARIMA vs IRR Curve")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("distribution_forecast.png")
#plt.show()
