CREATE TABLE STOPS(
    stop_id text PRIMARY KEY,
    stop_code text NOT NULL,
    stop_name text NOT NULL,
    stop_lat real NOT NULL,
    stop_lon real NOT NULL
);