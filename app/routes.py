def register_routes(api, app, root='api'):
    from app.widget import register_routes as attach_widget
    from app.fizz import register_routes as attach_fizz

    # Add routes
    attach_widget(api)
    attach_fizz(api)
