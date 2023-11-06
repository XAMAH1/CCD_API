from datetime import datetime

import jwt
from flask import request

from config import SECRET_KEY_PASSWORD


def save_err():
    try:
        current_user = jwt.decode(request.headers["Authorization"].split()[1], SECRET_KEY_PASSWORD,
                                  algorithms="HS256")
        date = datetime.today().strftime("%d-%m-%Y_%H-%M-%S")
        date1 = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
        f = open(rf"Error_log/{date}-user{current_user['ID']}.json", 'w+')
        f.write(str({
            "userId": current_user["ID"],
            "messagee": request.args["message"],
            "date": date1
        }))
        f.close()
    except Exception as e:
        print(e)
