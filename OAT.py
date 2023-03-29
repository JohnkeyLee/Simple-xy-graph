import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator, AutoDateFormatter
import matplotlib.dates as mdates

path = "G:/Shared drives/Developing Novel SOO to Operate Shades at Willis Tower/03 - Analysis & Report/06 - Paper (ENB)/Data/Plots/OAT.csv"

df = pd.read_csv(path, usecols=['Date/Time', 'Outdoor Temp', 'Averaged Temp'])
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
DateTime = df['Date/Time']
OutdoorTemp = df['Outdoor Temp']
AveragedTemp = df['Averaged Temp']

dt11 = datetime.datetime(2021, 5, 3, 0, 0)
dt12 = datetime.datetime(2022, 2, 21, 0, 0)
dt21 = datetime.datetime(2022, 2, 14, 0, 0)
dt22 = datetime.datetime(2022, 3, 7, 0, 0)
step1 = datetime.timedelta(weeks=2)
step2 = datetime.timedelta(weeks=1)

dateticklabels = pd.date_range(start=dt11, end=dt12, freq=step1).strftime('%Y-%m-%d-%H:%M').tolist()
dateticklabels += pd.date_range(start=dt21, end=dt22, freq=step2).strftime('%Y-%m-%d-%H:%M').tolist()

plt.style.use('classic')

fig, ax = plt.subplots()
ax.plot(DateTime, OutdoorTemp, color='k', label='Outdoor air temperature', linewidth=2)
ax.scatter(DateTime, AveragedTemp, marker='^', s=80 ,color='orange', label='Averaged Temp')
ax.set_xlim(DateTime.iloc[0], DateTime.iloc[-1])
ax.set_ylim([-30, 35])

ax.set_ylabel('Temperature (°C)', fontsize=20, labelpad=10)

ax.set_xticks(pd.to_datetime(dateticklabels, format='%Y-%m-%d-%H:%M'))

# date_format = DateFormatter('%Y-%m-%d')
date_format = DateFormatter('%b-%d')
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_tick_params(labelsize=15, labelrotation=30, pad=5)
ax.yaxis.set_tick_params(labelsize=15, pad=5)

ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

ax.xaxis.label.set_position((0.5, -1))
ax.yaxis.label.set_position((-0.1, 0.5))

ax.legend(handles=[ax.lines[0], ax.collections[0]], labels=['Outdoor air temperature', 'Averaged temp'], loc='upper right')

plt.tight_layout()
plt.show()