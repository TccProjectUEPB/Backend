from sanic import Sanic
from src.main.routes import ROUTES
from src.infrastructure.database.connection import init_models
from src.background.tasks.default_admin_task import DefaultAdminTask


app = Sanic("http")

app.blueprint(ROUTES, version=1)

@app.listener("before_server_start")
async def setup_db(app):
    await init_models()
    await DefaultAdminTask.run()
