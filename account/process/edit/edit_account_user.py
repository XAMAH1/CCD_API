from database.base import *
from flask import request
from account.get.account import account
import jwt
from config import SECRET_KEY_PASSWORD
from datetime import datetime
from datetime import timedelta
from calendar import monthrange
from datetime import datetime

current_year = datetime.now().year
month = datetime.now().month
days = monthrange(current_year, month)[1]
print(days)

def edit_process_account_edit(connect):
    args = request.args
    date = date_generate()
    command = update(account).values({"date_attachments": date["today"], "date_parish": date["next_today"]}).where(account.c.id == args["id"], account.c.login == args["login"])
    result = connect.execute(command)
    connect.commit()
    print(result.rowcount)
    if result.rowcount != 0:
        return account(connect)
    return {"success": False, "message": "Ошибка. У аккаунта уже установлен статус"}


def date_generate():
    now = datetime.now()
    current_year = datetime.now().year
    month = datetime.now().month
    days = monthrange(current_year, month)[1]
    run_at = now + timedelta(days=days+1)
    success_time = run_at.strftime("%d.%m.%Y")
    return {"today": now.strftime("%d.%m.%Y"), "next_today": success_time}