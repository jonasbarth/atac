CREATE TABLE TRIPS(
    trip_id text PRIMARY KEY,
    route_id text NOT NULL,
    service_id text NOT NULL,
    trip_headsign text NOT NULL,
    trip_short_name text NOT NULL,
    direction_id integer NOT NULL,
    block_id text NOT NULL,
    shape_id integer NOT NULL
);