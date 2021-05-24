from app.resources.user import user_bp


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(user_bp)
