import sqlite3 as sl

import pandas as pd

if __name__ == '__main__':

    stop_times = pd.read_csv("resources/static/stop_times.txt")
    stop_times = stop_times.drop(["pickup_type", "drop_off_type", "stop_headsign"], axis=1)
    stop_times = stop_times.set_index(["trip_id", "stop_id"])
    con = sl.connect('my-test.db')

    stop_times.to_sql("STOP_TIMES", con, if_exists="append")