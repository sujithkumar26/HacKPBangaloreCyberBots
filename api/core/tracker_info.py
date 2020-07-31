from db import mongo


class TrackerInfoCore:

    def insert_info_details(self, tracking_id, name, address, location_latitude, location_longitude, fence_radius):
        """
        Insert tracker info details to db
        """
        try:
            result = mongo.db.tracker_info.insert_one(
                {'tracking_id': tracking_id, 'name': name, 'address': address,
                 'location': {'latitude': location_latitude, 'longitude': location_longitude},
                 'fence_radius': fence_radius})
            return result
        except Exception as e:
            print(e)
            return -1
