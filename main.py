from flask import *
from threading import Thread

from account.replenishment.replenishment import replenishment
from database.base import base_connect
from user.autme.user import user_autme
import jwt
from config import SECRET_KEY_PASSWORD, version
from account.get.account import account
from account.edit.edit import edit
from examination.examination_config_start import config_start_exam
from account.process.process_edit import process_account_edit
from account.registration.registration_account import registration_new_account
from image.image import send_image

#print(jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6IlVlVWhMaWtGakJXWSJ9.PAB-eeq4kMz9LY0rY5FDEIB_lIm4RL8psrp8mfi-Zsc", key=SECRET_KEY_PASSWORD, algorithms=["HS256"]))
#print(jwt.encode({"password": "271004ккк"}, key=SECRET_KEY_PASSWORD, algorithm="HS256"))

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

@app.route("/account/replenishment", methods=["GET"])
def account_replenishment():
    return replenishment(connect)

@app.route('/server/photo', methods=['GET'])
def download_file():
    return send_image()

@app.route('/get/actual/version', methods=['GET'])
def send_version_actual():
    return {"version": version}

if __name__ == '__main__':
#    from rest import vost
    connect = base_connect()
#   vost(connect)
    print("Server started")
    t = Thread(target=config_start_exam, args=(connect,)).start()
    app.run(debug=True, use_reloader=False, host="65.21.114.247", port=4848)

