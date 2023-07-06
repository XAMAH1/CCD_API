from flask import *

from database.base import base_connect

app = Flask(__name__)

@app.route("/user/autme", methods=["GET"])
def autme_user():
    return {'success': True, 'message': "да"}

if __name__ == '__main__':
    connect = base_connect()
    print("Server started")
    app.run(debug=True)