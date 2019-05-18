from .model import Widget  # noqa
from .schema import WidgetSchema  # noqa
BASE_ROUTE = 'widget'


def register_routes(root_api, root='api'):
    from .controller import api as widget_api
    root_api.add_namespace(widget_api, path=f'/{root}/{BASE_ROUTE}')
    return root_api
