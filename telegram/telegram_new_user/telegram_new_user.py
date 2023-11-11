from database.base import *
from flask import request


def telegram_new_user(connect):
    args = request.json
    command = select(telegram_user).where(telegram_user.c.telegramId == args["userId"])
    result = connect.execute(command)
    for i in result:
        return {"success": False, "message": "Вы уже зарегестированы", "isAdmin": i[4]}
    command = select(telegram_user_expectation).where(telegram_user_expectation.c.telegramId == args["userId"])
    result = connect.execute(command)
    if result.rowcount != 0:
        return {"success": True, "message": "Ваши данные проходят проверку для регистрации, оиждайте"}
    command = insert(telegram_user_expectation).values(login=args["login"], telegramId=args["userId"], isAdmin=False)
    result = connect.execute(command)
    if result.rowcount != 0:
        connect.commit()
        return {"success": True, "message": "Ваши данные были направлены на регистрацию в системе"}