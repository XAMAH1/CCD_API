import jwt
from flask import request
from database.base import *
from config import SECRET_KEY_PASSWORD

def user_autme(connect):
    try:
        args = request.args
        command = select(autme_user).where(autme_user.c.login == args['login'])
        result = connect.execute(command)
        for current_user in result:
            password = jwt.decode(current_user[2], SECRET_KEY_PASSWORD, algorithms="HS256")
            if str(password["password"]) != str(args["password"]):
                return {"success": False, "message": "Неверный логин или пароль"}, 401
            token = jwt.encode({"ID": current_user[0]}, SECRET_KEY_PASSWORD, algorithm="HS256")
            return {"success": True, "message": token}, 200
        return {"success": False, "message": "Неверный логин или пароль"}, 401
    except Exception as e:
        print(e)
        return {"success": False, "message": "Возникла ошибка при авторизации"}, 404