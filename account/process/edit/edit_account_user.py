from flask import request
from account.get.account import account
from datetime import timedelta, datetime
from calendar import monthrange
from database.base import *

def edit_process_account_edit(connect):
    args = request.args
    date = date_generate()
    command = update(account).values({"date_attachments": date["today"], "date_parish": date["next_today"], "cach": int(request.args["cach"])}).where(account.c.login == args["login"])
    connect.execute(command)
    connect.commit()


def date_generate():
    now = datetime.now()
    current_year = datetime.now().year
    month = datetime.now().month
    days = monthrange(current_year, month)[1]
    run_at = now + timedelta(days=days+1)
    success_time = run_at.strftime("%d.%m.%Y")
    return {"today": now.strftime("%d.%m.%Y"), "next_today": success_time}