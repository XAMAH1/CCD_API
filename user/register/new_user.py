import jwt
from database.base import *
from flask import request
import json
import datetime
from config import SECRET_KEY_PASSWORD

def user_register(connect):
   try:
       data = json.loads(request.data)
       command = select(autme_user).where(autme_user.c.login == data["login"])
       result = connect.execute(command)
       for i in result:
           return {"success": False, "message": "Логин уже занят"}, 401
       password = jwt.encode({"password": data["password"]}, SECRET_KEY_PASSWORD, algorithm="HS256")
       date_today = datetime.datetime.today()
       command = insert(autme_user).values(login=data["login"], password=password, date_create=str(date_today))
       connect.execute(command)
       connect.commit()
       return {"success": True, "message": "Аккаунт успешно зарегистрирован"}, 200
   except Exception as e:
       print(e)
       return {"success": False, "message": "Возникла ошибка при регистрации"}, 404