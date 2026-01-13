import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load the dataset
# -----------------------------
df = pd.read_csv("tokyo_weather.csv")

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# Convert day column to datetime
df["date"] = pd.to_datetime(df["year"].astype(str) + "/" + df["day"])

# -----------------------------
# 1. Temperature Overview
# a. Average temperature for entire dataset
# -----------------------------
average_temp = df["temperature"].mean()
print(f"Average Temperature (Entire Dataset): {average_temp:.2f}°C")

# -----------------------------
# 2. Monthly Temperature
# a. Average temperature for each month
# -----------------------------
df["month"] = df["date"].dt.month
monthly_avg = df.groupby("month")["temperature"].mean()

print("\nAverage Temperature by Month:")
print(monthly_avg)

# b. Bar plot of monthly average temperature
plt.figure(figsize=(8, 5))
monthly_avg.plot(kind="bar", color="skyblue")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.title("Monthly Average Temperature in Tokyo")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Highs and Lows
# a. Hottest and coldest days
# -----------------------------
hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)

# -----------------------------
# 4. Temperature Trends
# a. Line graph of temperature over time
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["temperature"], color="red")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over Time in Tokyo")
plt.tight_layout()
plt.show()

# -----------------------------
# 4. b. Seasonal Average Temperature
# -----------------------------
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["month"].apply(get_season)
seasonal_avg = df.groupby("season")["temperature"].mean()

print("\nSeasonal Average Temperature:")
print(seasonal_avg)
