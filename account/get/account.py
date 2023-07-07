from account.get.check_account.check import check
from database.base import *
import jwt
from config import SECRET_KEY_PASSWORD
from flask import request

def account(connect):
    try:
        current_user = jwt.decode(request.headers["Authorization"].split()[1], SECRET_KEY_PASSWORD, algorithms="HS256")
        return check(connect, current_user["ID"])
    except:
        return {"success": False, "message": "Не валидный токен авторизации"}