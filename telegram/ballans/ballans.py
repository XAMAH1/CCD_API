from database.base import *
from flask import request


def ballans(connect):
    command = select(telegram_user).where(telegram_user.c.telegramId == request.json["userId"], telegram_user.c.isAdmin == True)
    result = connect.execute(command)
    if result.rowcount == 0:
        return {"success": False, "message": "Вы не являетесь администартором"}
    command = select(account)
    result = connect.execute(command)
    current_account = 0
    for i in result:
        current_account += int(i[6])
    return {"success": True, "ballans": f"На аккаунтах осталось {current_account}р валюты"}
