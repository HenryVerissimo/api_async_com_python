from src import create_app
from quart import Quart


def test_create_app_return_quart_object():
    app = create_app()
    assert type(app) is Quart


def test_app_import_name_is_src():
    app = create_app()
    assert app.import_name == "src"
