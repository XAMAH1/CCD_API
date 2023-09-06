from database.base import *
from config import SECRET_KEY_PASSWORD, SECRET_KEY_PASSWORD_ACCOUNT_GET
import jwt

def get_account_null(connect):
    command = select(account).where(account.c.date_attachments == Null)
    result = connect.execute(command)
    for i in result:
        password = jwt.decode(i[2], SECRET_KEY_PASSWORD, algorithms="HS256")
        token = jwt.encode({"password": password["password"]}, SECRET_KEY_PASSWORD_ACCOUNT_GET, algorithm="HS256")
        return "da"#{"id": i[0], "login": i[1], "password": token, "id_transaction": }
    return "net"