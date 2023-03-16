import requests
from google.transit import gtfs_realtime_pb2
from tinydb import TinyDB

if __name__ == '__main__':

    atac = TinyDB("atac.json")

    url = "https://dati.comune.roma.it/catalog/dataset/a7dadb4a-66ae-4eff-8ded-a102064702ba/resource/bf7577b5-ed26-4f50-a590-38b8ed4d2827/download/rome_trip_updates.pb"
    response = requests.get(url)

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)

    for entity in feed.entity:
        if entity.HasField('trip_update'):
            trip = entity.trip_update.trip
            trip_id = trip.trip_id
            start_time = trip.start_time
            start_date = trip.start_date
            route_id = trip.route_id

            stop_updates = []
            for stop_time_update in entity.trip_update.stop_time_update:
                stop_sequence = stop_time_update.stop_sequence
                delay = stop_time_update.arrival.delay
                time = stop_time_update.arrival.time
                uncertainty = stop_time_update.arrival.uncertainty
                stop_id = stop_time_update.stop_id

                stop_update = {"trip_id": trip_id, "start_time": start_time, "start_date": start_date,
                               "route_id": route_id, "stop_sequence": stop_sequence, "delay": delay, "time": time,
                               "uncertainty": uncertainty, "stop_id": stop_id}

                stop_updates.append(stop_update)

            atac.insert_multiple(stop_updates)

    atac.close()
