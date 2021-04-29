from flask import Flask


def init_application():
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    with app.app_context():
        from Application import routes
        from Application import api

        app.register_blueprint(routes.routes_blueprint)
        app.register_blueprint(api.api_blueprint)

        return app
