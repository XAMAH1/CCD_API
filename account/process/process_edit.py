from database.base import *
from flask import request
from account.get.account import account
import jwt
from config import SECRET_KEY_PASSWORD
from datetime import datetime

def process_account_edit(connect):
    current_user = jwt.decode(request.headers["Authorization"].split()[1], SECRET_KEY_PASSWORD, algorithms="HS256")
    args = request.args
    now = datetime.now()
    success_time = now.strftime("%d.%m.%Y %H:%M:%S")
    command = update(history_account).values({"success": "Выполнено", "date_expiration": success_time}).where(history_account.c.id == args["id_transaction"], history_account.c.id_user == current_user["ID"], history_account.c.success == "В процессе")
    result = connect.execute(command)
    connect.commit()
    print(result.rowcount)
    if result.rowcount != 0:
        return account(connect)
    return {"success": False, "message": "Ошибка. У аккаунта уже установлен статус"}
