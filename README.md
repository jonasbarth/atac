# ATAC
This is a small trial to gather some live data from ATAC services about delays.

# Data Source
The data comes from the transport section of [Roma Open Data](https://dati.comune.roma.it/catalog/dataset/c_h501-d-9000)

- [Static Data](https://dati.comune.roma.it/catalog/dataset/c_h501-d-9000/resource/266d82e1-ba53-4510-8a81-370880c4678f)
- [Real-Time Trip Updates](https://dati.comune.roma.it/catalog/dataset/c_h501-d-9000/resource/bf7577b5-ed26-4f50-a590-38b8ed4d2827)
- [Real-Time Vehicle Positions](https://dati.comune.roma.it/catalog/dataset/c_h501-d-9000/resource/d2b123d6-8d2d-4dee-9792-f535df3dc166)

# Trip Updates
## Data Format
The data is in the [GTFS](https://developers.google.com/transit/gtfs-realtime) format, which is a realtime traffic
data format developed by google.

GTFS is based on the google [protocol buffer](https://protobuf.dev/), which is a language neutral
structured data format. The file provided by Roma Open Data is a protocol buffer `.pb` file, which contains
information about *trip updates*.

The structure of the protocol buffer that is provided by ATAC, is that of the [gtfs-realtime.proto](gtfs-realtime.proto) format.

## Fetching Data
Roma Open Data continuously updates the trip updates file at [this location](https://dati.comune.roma.it/catalog/dataset/a7dadb4a-66ae-4eff-8ded-a102064702ba/resource/bf7577b5-ed26-4f50-a590-38b8ed4d2827/download/rome_trip_updates.pb)
so all that needs to be done is to fetch it once a minute or so.

## Parsing Data
To read the protocol buffer, you will need to install the `protobuf` and `gtfs-realtime-bindings`  packages
for parsing the buffer and for generating the python bindings.

### Opening File
The `.pb` file needs to be opened as a binary file, using the `b` argument in the `open` function and read using the
**gtfs python binding** by Google. The `FeedMessage` is the top level element in the protocol buffer, so we need to 
access it first.

```python
from google.transit import gtfs_realtime_pb2

with open('rome_trip_updates.pb', 'rb') as file:
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(file.read())
```

### Getting Trip Updates
To get the trip updates, we need to move through the nested structure of the protocol buffer. Below is a `yaml` representation
of the elements of interest. 
```yaml
FeedMessage:
  FeedEntity:
    TripUpdate:
      StopTimeEvent:
      StopTimeUpdate:
```

Example for getting the delay.
```python
for entity in feed.entity:
    if entity.HasField('trip_update'):
        entity.trip_update.stop_time_update.delay
```

# Questions

## Is there a schedule?
Yes, in the GTFS-static file we have the [schedule](resources/static/stop_times.txt) and many other things. 
Using this, we can calculate the true delay.
Other static data like routes, trips, etc. can be found [here](resources/static).

## How can we know the actual arrival time?
We have the latitude and longitude of each [station/stop](resources/static/stops) and the live location of vehicles 
from the [vehicle positions](https://dati.comune.roma.it/catalog/dataset/c_h501-d-9000/resource/d2b123d6-8d2d-4dee-9792-f535df3dc166) 
which is updated roughly once a minute, we need to compare the current location with the location 
of the next stop of the vehicle.