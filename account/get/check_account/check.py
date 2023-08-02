import random
from database.base import *
from account.get.recording.recording import record
import datetime

def check(connect):
    try:
        all_account = all_account_get(connect)
        passed_account = passed_account_get(connect)
        if len(all_account) == len(passed_account):
            return {"success": True, "message": "account undefined"}
        job = True
        while job:
            current_account = random.choice(all_account)
            if current_account not in passed_account:
                record(connect, current_account)
                return current_account
    except:
        return {"success": True, "message": "not account"}

def all_account_get(connect):
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    command = select(account).where(account.c.date_parish == current_date, account.c.access_modifier == "user")
    result = connect.execute(command)
    current_account = []
    for i in result:
        current_account.append(i[1])
    return current_account

def passed_account_get(connect):
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    command = select(history_account).where(history_account.c.date_parish == current_date)
    result = connect.execute(command)
    current_account = []
    for i in result:
        if i[3] != "Завершено" or i[3] != "В процессе":
            current_account.append(i[1])
    return current_account