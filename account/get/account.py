from account.get.check_account.check import check
from database.base import *

def account(connect):
    return check(connect)


def acc(connect):
    command = update(history_account).values({"success": "авц"}).where(history_account.c.id == 1)
    connect.execute(command)
    connect.commit()