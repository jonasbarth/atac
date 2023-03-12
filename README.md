# ATAC
This is a small trial to gather some live data from ATAC services about delays.

# Data Source
The data comes from the transport section of [Roma Open Data](https://dati.comune.roma.it/catalog/dataset/c_h501-d-9000)

# Data Format
The data is in the [GTFS](https://developers.google.com/transit/gtfs-realtime) format, which is a realtime traffic
data format developed by google.

GTFS is based on the google [protocol buffer](https://protobuf.dev/), which is a language neutral
structured data format. The file provided by Roma Open Data is a protocol buffer `.pb` file, which contains
information about *trip updates*.

The structure of the protocol buffer that is provided by ATAC, is that of the [gtfs-realtime.proto](gtfs-realtime.proto) format.

# Fetching Data
Roma Open Data continuously updates the trip updates file at [this location](https://dati.comune.roma.it/catalog/dataset/a7dadb4a-66ae-4eff-8ded-a102064702ba/resource/bf7577b5-ed26-4f50-a590-38b8ed4d2827/download/rome_trip_updates.pb)
so all that needs to be done is to fetch it once a minute or so.

# Reading Data
To read the protocol buffer, you will need to install the `protobuf` and `gtfs-realtime-bindings`  packages
for parsing the buffer and for generating the python bindings.