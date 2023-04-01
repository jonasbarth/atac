import sqlite3 as sl

import pandas as pd

if __name__ == '__main__':

    stop_times = pd.read_csv("resources/static/stops.txt")

    stop_times = stop_times.drop(["stop_desc", "stop_url", "wheelchair_boarding", "stop_timezone", "location_type", "parent_station"], axis=1)
    stop_times = stop_times.set_index(["stop_id"])
    con = sl.connect('my-test.db')

    stop_times.to_sql("STOPS", con, if_exists="append")