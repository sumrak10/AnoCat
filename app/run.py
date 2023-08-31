import os

import uvicorn

from src.config import settings


# os.system('python -m alembic revision --autogenerate -m "init"')
# os.system('python -m alembic upgrade head')

if __name__ == '__main__':
    if settings.NOT_SEND_CERT:
        uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT)
    else:
        uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT, ssl_keyfile="rootCA.key", ssl_certfile="rootCA.pem")