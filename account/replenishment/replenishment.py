import jwt
from flask import request

from account.replenishment.account_get.get_account_null import get_account_null
from config import SECRET_KEY_PASSWORD


def replenishment(connect):
    try:
        current_user = jwt.decode(request.headers["Authorization"].split()[1], SECRET_KEY_PASSWORD, algorithms="HS256")
        return get_account_null(connect, current_user["ID"])
    except:
        return {"success": False, "message": "Не валидный токен авторизации"}