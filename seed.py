import sqlite3
import csv

conn = sqlite3.connect("weather.db")
cur = conn.cursor()

def create_tables():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather_stations (
        code TEXT PRIMARY KEY,
        name TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather_readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        station TEXT,
        AWND REAL,
        PRCP REAL,
        SNOW REAL,
        TMAX REAL,
        TMIN REAL,
        FOREIGN KEY (station) REFERENCES weather_stations(code)
    );
    """)


insert_stations_query = """
INSERT INTO weather_stations (code, name) VALUES (?, ?);
"""

insert_readings_query = """
INSERT INTO weather_readings (date, station, AWND, PRCP, SNOW, TMAX, TMIN) VALUES (?, ?, ?, ?, ?, ?, ?);
"""

all_files = ["data/1-1-2017_12-31-2019.csv", 
         "data/1-1-2020_12-31-2022.csv", 
         "data/1-1-2023_today.csv"]
station_list = []
for file in all_files:
    with open(file, 'r') as file:
        reader = csv.reader(file)

        keys = {}
        header = next(reader)
        for i, col in enumerate(header):
            keys[col] = i

        for row in reader:
            station_code = row[0]
            station_name = row[1]

            if station_code not in station_list:
                print(station_code)
                #cur.execute(insert_stations_query, (station_code, station_name))
                station_list.append(station_code)

            cur.execute(insert_readings_query, 
                        (row[keys['DATE']],
                         row[keys['STATION']],
                         row[keys['AWND']],
                         row[keys['PRCP']],
                         row[keys['SNOW']],
                         row[keys['TMAX']],
                         row[keys['TMIN']]))
            

            




conn.commit()
conn.close()