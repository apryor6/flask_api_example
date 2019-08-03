from .model import Widget  # noqa
from .schema import WidgetSchema  # noqa

BASE_ROUTE = "widget"


def register_routes(api, app, root="api"):
    from .controller import api as widget_api

    api.add_namespace(widget_api, path=f"/{root}/{BASE_ROUTE}")
