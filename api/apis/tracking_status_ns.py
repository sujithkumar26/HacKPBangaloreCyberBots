from flask_restx import Namespace, Resource, reqparse

tracking_status_ns = Namespace("Tracking Status", description="Endpoints related to tracking status")


@tracking_status_ns.route("/status")
class TrackerInfo(Resource):
    @tracking_status_ns.response(200, "Success", headers={'Content-Type': 'application/json'})
    def get(self):
        return {'status': 'success'}
