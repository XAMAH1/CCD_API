import datetime

import jwt
from database.base import *
from config import SECRET_KEY_PASSWORD
from flask import *


def new_account_system(connect):
    command = select(telegram_user).where(telegram_user.c.telegramId == request.json["userId"],
                                          telegram_user.c.isAdmin == True)
    result = connect.execute(command)
    if result.rowcount == 0:
        return {"success": False, "message": "Вы не являетесь администартором"}
    command = select(autme_user).where(autme_user.c.login == request.json["login"])
    result = connect.execute(command)
    if result.rowcount != 0:
        return {"success": False, "message": "Указанный вами логин уже занят"}
    if len(request.json["login"]) < 5 or len(request.json["password"]) < 5:
        return {"success": False, "message": "Проверьте вводимые данные (логин и пароль от 5 символов)"}
    password = jwt.encode({"password": request.json["password"]}, SECRET_KEY_PASSWORD, algorithm="HS256")
    success_time = datetime.datetime.today().strftime("%d.%m.%Y")
    command = insert(autme_user).values(login=request.json["login"], password=password, role="user", data_create=success_time)
    result = connect.execute(command)
    if result.rowcount != 0:
        connect.commit()
        return {"success": True, "message": "Успешное добавление нового пользователя"}
    return {"success": False, "message": "В чем то ошибка, пробуй еще черт"}
