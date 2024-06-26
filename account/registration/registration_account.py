from database.base import *
from flask import request
from account.get.account import account
import jwt
from config import SECRET_KEY_PASSWORD
from string import ascii_letters
import random
from database.base import *

def registration_new_account(connect):
    login = ''.join([random.choice(ascii_letters) for i in range(16)]) + "3"
    password_open = ''.join([random.choice(ascii_letters) for i in range(12)])
    password = jwt.encode({"password": password_open}, SECRET_KEY_PASSWORD, algorithm="HS256")
    command = insert(account).values(login=login, password=password, access_modifier="user")
    result = connect.execute(command)
    connect.commit()
    print(result.rowcount)
    if result.rowcount != 0:
        return {"success": True, "message": "Аккаунт создан", "login": login, "password": password_open}
    return {"success": False, "message": "Ошибка"}
