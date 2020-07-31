from flask_restx import Namespace, Resource, reqparse

from core.tracker_info import TrackerInfoCore

tracker_info_ns = Namespace("Tracker Info", description="Endpoints related to tracker information")

req_parser = reqparse.RequestParser()
req_parser.add_argument('tracking_id', type=str, help='Tracking ID for user')
req_parser.add_argument('name', type=str, help='Name of user to be tracked')
req_parser.add_argument('address', type=str, help='Address of user to be tracked')
req_parser.add_argument('location-latitude', type=str, help='Current location - latitude of user to be tracked')
req_parser.add_argument('location-longitude', type=str, help='Current location - longitude of user to be tracked')
req_parser.add_argument('fence_radius', type=str, help='Radius from current location of user to be tracked')


@tracker_info_ns.route("/info")
class TrackerInfo(Resource):
    @tracker_info_ns.response(200, "Success", headers={'Content-Type': 'application/json'})
    def get(self):
        return {'status': 'success'}

    @tracker_info_ns.expect(req_parser)
    @tracker_info_ns.response(200, "Success", headers={'Content-Type': 'application/json'})
    def post(self):
        try:
            args = req_parser.parse_args()
            tracking_id = args.get('tracking_id')
            name = args.get('name')
            address = args.get('address')
            location_latitude = args.get('location-latitude')
            location_longitude = args.get('location-longitude')
            fence_radius = args.get('fence_radius')
            result = TrackerInfoCore().insert_info_details(tracking_id, name, address, location_latitude,
                                                           location_longitude, fence_radius)
            if result != -1:
                return {'status': 'success', 'msg': 'Data inserted successfully'}
            return {"status": "failed"}
        except Exception as e:
            print(e)
            return {"status": "failed"}
