import sqlite3 as sl

import pandas as pd

if __name__ == '__main__':

    trips = pd.read_csv("resources/static/trips.txt")
    trips = trips.drop(["wheelchair_accessible", "exceptional"], axis=1)
    trips = trips.set_index(["trip_id"])
    con = sl.connect('my-test.db')

    trips.to_sql("TRIPS", con, if_exists="append")