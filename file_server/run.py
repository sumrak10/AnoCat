import uvicorn

from src.config import settings



if __name__ == '__main__':
    uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT)

# import multiprocessing

# from gunicorn.app.wsgiapp import WSGIApplication


# class StandaloneApplication(WSGIApplication):
#     def __init__(self, app_uri, options=None):
#         self.options = options or {}
#         self.app_uri = app_uri
#         super().__init__()

#     def load_config(self):
#         config = {
#             key: value
#             for key, value in self.options.items()
#             if key in self.cfg.settings and value is not None
#         }
#         for key, value in config.items():
#             self.cfg.set(key.lower(), value)


# def run():
#     options = {
#         "bind": "0.0.0.0:8001",
#         "workers": (multiprocessing.cpu_count() * 2) + 1,
#         "worker_class": "uvicorn.workers.UvicornWorker",
#     }
#     StandaloneApplication("src.main:app", options).run()