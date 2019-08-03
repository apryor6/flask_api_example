def register_routes(api, app, root="api"):
    from app.widget import register_routes as attach_widget
    from app.fizz import register_routes as attach_fizz
    from app.other_api import register_routes as attach_other_api
    from app.third_party.app import create_bp

    # Add routes
    attach_widget(api, app)
    attach_fizz(api, app)
    attach_other_api(api, app)
    app.register_blueprint(create_bp(), url_prefix="/third_party")
