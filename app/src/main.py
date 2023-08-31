from fastapi import FastAPI


app = FastAPI()



from .anocat.webhook_router import router as bot_webhook_router
app.include_router(bot_webhook_router)