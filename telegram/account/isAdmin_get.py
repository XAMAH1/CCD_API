from flask import request
from database.base import *

def isAdmin_get(connect):
    command = select(telegram_user).where(telegram_user.c.isAdmin == True)
    result = connect.execute(command)
    user_admin = []
    for i in result:
        user_admin.append(i[2])
    return {"success": True, "account": user_admin}
