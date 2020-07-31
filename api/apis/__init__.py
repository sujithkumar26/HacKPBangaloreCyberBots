from flask_restx import Api
from .tracker_info_ns import tracker_info_ns
from .tracking_status_ns import tracking_status_ns

api = Api(
    title='Virtual Presence API',
    version='1.0',
    description='API backend for Virtual Presence'
)

api.add_namespace(tracker_info_ns, path='/tracker')
api.add_namespace(tracking_status_ns, path='/tracker')
