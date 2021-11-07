from app.models.models_windbox import Windbox
from tests.api.endpoint import BaseTestEndpoint


class TestWindbox(BaseTestEndpoint):
    create_data = {"hostname": "windbox01.windreserve.de"}
    update_data = {"hostname": "windbox02.windreserve.de"}
    endpoint = "/windbox"
    create_obj_cls = Windbox
