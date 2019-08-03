BASE_ROUTE = "fizz"


def register_routes(api, app, root="api"):
    from .fizzbar.controller import api as fizzbar_api
    from .fizzbaz.controller import api as fizzbaz_api

    api.add_namespace(fizzbar_api, path=f"/{root}/{BASE_ROUTE}/fizzbar")
    api.add_namespace(fizzbaz_api, path=f"/{root}/{BASE_ROUTE}/fizzbaz")
