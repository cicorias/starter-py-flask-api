# https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/

from flask import Flask as BaseFlask, session
from flask.helpers import get_debug_flag


from .config import (
    BaseConfig,
    DevConfig,
    ProdConfig,
)
def create_app():
    """Creates a pre-configured Flask application.

    Defaults to using :class:`backend.config.ProdConfig`, unless the
    :envvar:`FLASK_DEBUG` environment variable is explicitly set to "true",
    in which case it uses :class:`backend.config.DevConfig`. Also configures
    paths for the templates folder and static files.
    """
    return _create_app(
        DevConfig if get_debug_flag() else ProdConfig,
        template_folder=TEMPLATE_FOLDER,
        static_folder=STATIC_FOLDER,
        static_url_path=STATIC_URL_PATH
    )
