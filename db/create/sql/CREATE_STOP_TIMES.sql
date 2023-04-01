CREATE TABLE STOP_TIMES(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id text NOT NULL,
    arrival_time text NOT NULL,
    departure_time text NOT NULL,
    stop_id integer NOT NULL,
    stop_sequence integer not NULL,
    shape_dist_traveled integer,
    timepoint integer,
    FOREIGN KEY (trip_id) REFERENCES TRIPS (trip_id),
    FOREIGN KEY (stop_id) REFERENCES STOPS (stop_id)
);