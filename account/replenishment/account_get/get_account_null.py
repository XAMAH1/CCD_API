import random
from datetime import datetime

from account.get.check_account.check import get_account_settings
from database.base import *
from config import SECRET_KEY_PASSWORD, SECRET_KEY_PASSWORD_ACCOUNT_GET
import jwt
from account.get.recording.recording import record

def get_account_null_all(connect):
    command = select(account).where(account.c.date_attachments == "null")
    result = connect.execute(command)
    current_account = []
    for i in result:
        current_account.append(i[1])
    return current_account

def passed_account_get(connect):
    now = datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    command = select(history_account).where(history_account.c.date_parish == current_date, history_account.c.type_operation == "Пополнение")
    result = connect.execute(command)
    current_account = []
    for i in result:
        if i[3] == "Выполнено" or i[3] == "В процессе":
            current_account.append(i[1])
    return current_account

def get_account_null(connect):
    all_account = get_account_null_all(connect)
    passed_account = passed_account_get(connect)
    if len(all_account) <= len(passed_account):
        return {"success": True, "message": "аккаунтов больше нет"}

    job = True
    while job:
        current_account = random.choice(all_account)
        if current_account not in passed_account:
            id = record(connect, current_account, 1, "Пополнение")
            return get_account_settings(connect, current_account, id)
    return {"success": True, "message": "аккаунтов больше нет"}