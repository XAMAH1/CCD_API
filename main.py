from flask import *
from threading import Thread

from database.base import base_connect
from user.autme.user import user_autme
import jwt
from config import SECRET_KEY_PASSWORD
from account.get.account import account
from account.edit.edit import edit
from examination.examination_config_start import config_start_exam
from account.process.process_edit import process_account_edit
from account.registration.registration_account import registration_new_account

token = jwt.encode({"password": "271004"}, SECRET_KEY_PASSWORD, algorithm="HS256")
print(token)

app = Flask(__name__)

@app.route("/user/autme", methods=["GET"])
def autme_user():
    return user_autme(connect)

@app.route("/account/get", methods=["GET"])
def account_get_random():
    return account(connect)

@app.route("/account/edit", methods=["GET"])
def err_account():
    return edit(connect)

@app.route("/account/process", methods=["GET"])
def account_process():
    return process_account_edit(connect)

@app.route("/account/registration", methods=["GET"])
def account_registration():
    return registration_new_account(connect)

if __name__ == '__main__':
    connect = base_connect()
    print("Server started")
    t = Thread(target=config_start_exam, args=(connect,)).start()
    app.run(debug=True, use_reloader=False)