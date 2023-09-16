import hmac
import hashlib
from urllib.parse import unquote 

from src.anocat.bot.config import settings as bot_settings



def validateInitData(init_data, token=bot_settings.TOKEN, c_str="WebAppData"):
    """
    Validates the data received from the Telegram web app, using the
    method documented here: 
    https://core.telegram.org/bots/webapps#validating-data-received-via-the-web-app

    init_data - the query string passed by the webapp
    token - Telegram bot's token
    c_str - constant string (default = "WebAppData")
    """
    init_data_list = sorted(
        [chunk.split("=") for chunk in unquote(init_data).split("&")], 
        key=lambda x: x[0]
    )
    hash_str = [rec[1] for rec in init_data_list if rec[0] == "hash"][0]
    init_data = "\n".join([f"{rec[0]}={rec[1]}" for rec in init_data_list
        if rec[0] != "hash"])

    secret_key = hmac.new(c_str.encode(), token.encode(),
        hashlib.sha256 ).digest()
    data_check = hmac.new( secret_key, init_data.encode(),
        hashlib.sha256)

    return data_check.hexdigest() == hash_str