from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/web_app",
    tags=['web_app']
)

@router.get(f"/test")
async def test():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <script src="https://telegram.org/js/telegram-web-app.js"></script>
        </head>
        <body style="width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center;">
            <h1>Hello world!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)