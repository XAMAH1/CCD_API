from flask import *

from database.base import base_connect
from user.autme.user import user_autme
import jwt
from config import SECRET_KEY_PASSWORD

token = jwt.encode({"password": 123}, SECRET_KEY_PASSWORD, algorithm="HS256")
print(token)

app = Flask(__name__)

@app.route("/user/autme", methods=["GET"])
def autme_user():
    return user_autme(connect)

if __name__ == '__main__':
    connect = base_connect()
    print("Server started")
    app.run(debug=True)