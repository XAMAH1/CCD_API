from flask import *
from threading import Thread

from account.replenishment.replenishment import replenishment
from database.base import base_connect
from user.autme.user import user_autme
import jwt
from config import SECRET_KEY_PASSWORD
from account.get.account import account
from account.edit.edit import edit
from examination.examination_config_start import config_start_exam
from account.process.process_edit import process_account_edit
from account.registration.registration_account import registration_new_account


print(jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6InNxdnp0bHBtcG9wbiJ9.BF68y3I0dFiYDbMklnSPLNzBx2X_f3YAjR3Ks5G0vu8", key=SECRET_KEY_PASSWORD, algorithms=["HS256"]))

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

@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'No filename provided'}), 400

    try:
        return send_file(filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    connect = base_connect()
    print("Server started")
    t = Thread(target=config_start_exam, args=(connect,)).start()
    app.run(debug=True, use_reloader=False, host="65.21.114.247", port=4848)

