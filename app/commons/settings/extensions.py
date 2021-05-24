"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from commons.apispec import APISpecExt


db = SQLAlchemy()
migrate = Migrate()
apispec = APISpecExt()
