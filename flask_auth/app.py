import logging
import os
import sys

# Для дебага.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(f'{BASE_DIR}\\flask_auth')
# logging.error('-- DEBUG -- BASE DIR -- %s',  BASE_DIR)
# logging.error('-- DEBUG -- PYTHONPATH -- %s',  sys.path)


from api.v1.auth import auth
from api.v1.role import role
from core.config import app, settings
from db.db import init_db
from docs.app import init_docs
from services.jwt import *  # Регистрируем JWT

init_db()
app.register_blueprint(role, url_prefix="/api/v1")
app.register_blueprint(auth, url_prefix="/api/v1")
init_docs()

if settings.DEBUG:
    from create_superuser import create_superuser
    create_superuser()


def main():
    app.run()


if __name__ == '__main__':
    main()
