from quart import Quart
from typing import Optional

from .routes import users_bp


def create_app(config_class: Optional[object] = None) -> Quart:
    """Create and return a application instance"""

    app = Quart(__name__)
    if config_class:
        app.config.from_object(config_class)

    app.register_blueprint(users_bp, url_prefix="/users")

    return app
