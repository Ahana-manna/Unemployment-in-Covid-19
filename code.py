import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Unemployment in India.csv')

data.columns = data.columns.str.strip()

data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

print(data.info())
print(data.head())

# Plot unemployment rate over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=data, marker='o', color='b')
plt.title('Unemployment Rate Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Unemployment Rate (%)', fontsize=14)
plt.grid(True)
plt.show()

# Analyze statistics
print("Descriptive Statistics:\n", data['Estimated Unemployment Rate (%)'].describe())

# Optional: Highlight COVID-19 period
covid_start = '2020-03-01'
covid_end = '2022-12-31'
covid_data = data[(data['Date'] >= covid_start) & (data['Date'] <= covid_end)]

plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=covid_data, marker='o', color='r')
plt.title('Unemployment Rate During COVID-19', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Unemployment Rate (%)', fontsize=14)
plt.grid(True)
plt.show()
