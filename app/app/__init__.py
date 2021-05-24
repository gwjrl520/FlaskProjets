from flask import Flask

from commons.settings.extensions import apispec
from commons.settings.extensions import db
from commons.settings.extensions import migrate
from commons.settings.config import config_map
from app.resources import register_blueprints


def create_app(config_name):
    """Application factory, used to create application"""
    app = Flask(__name__, static_folder="../static", template_folder="..")
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    configure_extensions(app)
    configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )
