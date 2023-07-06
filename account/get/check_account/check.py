import random
from database.base import *
from account.get.recording.recording import record

def check(connect):
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

def all_account_get(connect):
    command = select(account)
    result = connect.execute(command)
    current_account = []
    for i in result:
        current_account.append(i[1])
    return current_account

def passed_account_get(connect):
    command = select(history_account)
    result = connect.execute(command)
    current_account = []
    for i in result:
        current_account.append(i[1])
    return current_account