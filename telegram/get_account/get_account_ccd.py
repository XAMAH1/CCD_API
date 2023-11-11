from flask import request
from database.base import *
from flask import jsonify


def get_account_ccd(connect):
    args = request.json
    command = select(telegram_user).where(telegram_user.c.telegramId == args["userId"], telegram_user.c.isAdmin == True)
    result = connect.execute(command)
    if result.rowcount == 0:
        return {"success": False, "message": "Вы не являетесь администартором"}
    command = select(account)
    result = connect.execute(command)
    count_account = 0
    for i in result:
        count_account += 1
    return {"success": True, "account": count_account}
