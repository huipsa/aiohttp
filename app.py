from app import create_app
from aiohttp import web
import os

if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
