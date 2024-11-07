import pandas as pd
import matplotlib.pyplot as plt
air_data = pd.read_csv('delhi_aqi.csv') #the data for AQI
weather_data = pd.read_csv('delhi_weather.csv') #the data for weather
merged = pd.merge(air_data, weather_data, on=['date']) #merging the data with date as primary key
#creating a scatter plot
plt.figure(figsize=(10, 6))
colors = ['red' if value > 250 else 'blue' for value in merged['pm2.5']]
plt.scatter(merged[' temperature'], merged['pm2.5'], color=colors, alpha=0.5)
plt.title('Plot for Temperature VS PM2.5 Levels in Delhi')
plt.xlabel('Temperature (C)')
plt.ylabel('PM2.5 Levels (microgram/m³)')
plt.grid(True)
plt.show()

