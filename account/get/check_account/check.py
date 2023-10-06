import random
from database.base import *
from account.get.recording.recording import record
import datetime
from flask import request
from config import SECRET_KEY_PASSWORD, SECRET_KEY_PASSWORD_ACCOUNT_GET
import jwt

def check(connect, id):
    try:
        all_account = all_account_get(connect)
        passed_account = passed_account_get(connect)
        if len(all_account) <= len(passed_account):
            return {"success": True, "message": "аккаунтов больше нет"}
        job = True
        while job:
            current_account = random.choice(all_account)
            if current_account not in passed_account:
                id = record(connect, current_account, id, "Процент")
                return get_account_settings(connect, current_account, id)
    except:
        return {"success": True, "message": "аккаунтов больше нет"}

def get_account_settings(connect, login, id_transaction):
    command = select(account).where(account.c.login == str(login))
    result = connect.execute(command)
    for i in result:
        password = jwt.decode(i[2], SECRET_KEY_PASSWORD, algorithms="HS256")
        token = jwt.encode({"password": password["password"]}, SECRET_KEY_PASSWORD_ACCOUNT_GET, algorithm="HS256")
        return {"id": i[0], "login": i[1], "password": token, "id_transaction": id_transaction}

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
        if i[3] == "Выполнено" or i[3] == "В процессе":
            current_account.append(i[1])
    return current_account