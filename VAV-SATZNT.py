import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator, AutoDateFormatter
import matplotlib.dates as mdates

path = "G:/Shared drives/Developing Novel SOO to Operate Shades at Willis Tower/03 - Analysis & Report/06 - Paper (ENB)/Data/Plots/VAV-SATZNT.csv"

df = pd.read_csv(path, usecols=['Date', 'SA-T', 'ZN-T'])
df['Date'] = pd.to_datetime(df['Date'])
DateTime = df['Date']
SupplyTemp = df['SA-T']
ZoneTemp = df['ZN-T']

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
ax.plot(DateTime, ZoneTemp, color='gray', label='ZN-T', linewidth=2)
ax.plot(DateTime, SupplyTemp, color='k', label='SA-T', linewidth=2)
ax.set_xlim(DateTime.iloc[0], DateTime.iloc[-1])
ax.set_ylim([14, 30])

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

ax.legend(loc='upper right', ncol=2)

plt.tight_layout()
plt.show()