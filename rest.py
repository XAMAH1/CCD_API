import json

import jwt

from config import SECRET_KEY_PASSWORD
from database.base import *

def vost(connect):
    text = open("C:\\Users\\Admin\\Desktop\\ttt\\account.txt", 'r').read()
    text = text.split('!')
    for i in text:
        t = i.split(",")
        print(f"""|{t[2][1:].split("'")[3]}|""")
        password = jwt.encode({"password": t[2][1:].split("'")[3]}, SECRET_KEY_PASSWORD, algorithm="HS256")
        command = insert(account).values(login=t[1][1:], password=password, access_modifier=t[3][1:],
                                         date_attachments=t[4][1:], date_parish=t[5][1:len(t[5])-1])
        result = connect.execute(command)
        connect.commit()

        print(f"|{t[1:]}|")