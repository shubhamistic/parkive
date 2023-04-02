import sqlite3
from datetime import date, datetime


conn = sqlite3.connect('models/record.sqlite', check_same_thread=False)
cur = conn.cursor()

# getting current date
# date format: YYYY-MM-DD
current_date = str(date.today()).replace('-', '_')

table_name = "record_" + current_date

# creating a table with current date as "record_date"
cur.execute(f"CREATE TABLE IF NOT EXISTS " + table_name + " (" +
            """ "lot_id"	TEXT NOT NULL,
                "lane_id"	TEXT NOT NULL,
                "spot_id"	TEXT NOT NULL,
                "in_time"	TEXT NOT NULL,
                "out_time"	TEXT
            );""")
conn.commit()


def getCurrentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def createEntry(lot_id, lane_id, spot_id):
    cur.execute(f" INSERT INTO {table_name}"
                f" (lot_id, lane_id, spot_id, in_time)"
                f" VALUES ('{lot_id}', '{lane_id}', '{spot_id}', '{getCurrentTime()}');")
    conn.commit()


def setOutTime(lot_id, lane_id, spot_id):
    cur.execute(f" UPDATE {table_name}"
                f" SET out_time = '{getCurrentTime()}'"
                f" where lot_id = '{lot_id}' AND lane_id = '{lane_id}' AND spot_id = '{spot_id}';")
    conn.commit()
