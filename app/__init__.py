from aiohttp import web
from app.routes import setup_routes
from app.config import Config
from app.database import init_db


def create_app():
    app = web.Application()
    app['config'] = Config()

    init_db(app)

    setup_routes(app)

    return app
