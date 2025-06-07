import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime


conn = sqlite3.connect("weather.db")
cur = conn.cursor()

query = """
SELECT date, TMAX FROM weather_readings
WHERE station = 'USW00094728'
ORDER BY date ASC
"""

cur.execute(query)
data = cur.fetchall()
conn.close()
# date_data = []

dates = []
values = []

for x in data:
    date = datetime.strptime(x[0], "%Y-%m-%d")
    value = x[1]
    print(date, value)

    dates.append(date)
    values.append(values)