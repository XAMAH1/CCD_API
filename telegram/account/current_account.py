import jwt
from flask import request
from database.base import *
from flask import jsonify
from config import SECRET_KEY_PASSWORD


def get_current_account_ccd(connect):
    args = request.json
    command = select(telegram_user).where(telegram_user.c.telegramId == args["userId"], telegram_user.c.isAdmin == True)
    result = connect.execute(command)
    if result.rowcount == 0:
        return {"success": False, "message": "Вы не являетесь администартором"}
    command = select(account).where(account.c.id == request.args["AccountId"])
    result = connect.execute(command)
    for i in result:
        password = jwt.decode(i[2], SECRET_KEY_PASSWORD, algorithms=["HS256"])
        return {"success": True, "account": f"Логин {i[1]}\nПароль: {password['password']}\nБалланс аккаунта: {i[6]}"}
    return {"success": True, "account": f"Указанного вами аккаунта не найдена"}