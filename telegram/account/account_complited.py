from datetime import datetime

from flask import request

from database.base import *


def admin_complited(connect, user_id):
    current_date = datetime.now().strftime("%d.%m.%Y")
    command = select(history_account).where(history_account.c.date_parish == current_date,
                                            history_account.c.success == "Выполнено",
                                            history_account.c.id_user == user_id
                                            )
    result = connect.execute(command)
    count_account_completed = 0
    for i in result:
        count_account_completed += 1
    command = select(autme_user).where(autme_user.c.id == user_id)
    result = connect.execute(command)
    for i in result:
        return {"success": True, "message": f"Аккаунт с логином {i[1]} прошел {count_account_completed} акк"}


def user_complited(connect, telegram_id):
    current_date = datetime.now().strftime("%d.%m.%Y")
    command = select(telegram_user).where(telegram_user.c.telegramId == telegram_id)
    result = connect.execute(command)
    for i in result:
        if len(i[3]) < 1:
            return {"success": True, "message": f"К вашему телеграмму еще не привязан аккаунт"}
        command = select(history_account).where(history_account.c.date_parish == current_date,
                                                history_account.c.success == "Выполнено",
                                                history_account.c.id_user == i[3]
                                                )
        result = connect.execute(command)
        count_account_completed = 0
        for i in result:
            count_account_completed += 1
        return {"success": True, "message": f"Вы прошли {count_account_completed} аккаунта"}

def account_complited(connect):
    if 'user' in request.args:
        command = select(telegram_user).where(telegram_user.c.telegramId == request.json["userId"],
                                              telegram_user.c.isAdmin == True)
        result = connect.execute(command)
        if result.rowcount != 0:
            return admin_complited(connect, request.args["user"])
    return user_complited(connect, request.json["userId"])