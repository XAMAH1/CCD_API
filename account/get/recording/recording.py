from database.base import *
from flask import request
import datetime
def record(connect, login, id):
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    current_time = now.strftime("%H:%M:%S")
    command = insert(history_account).values(login=login, id_user=id, date_parish=current_date, time_parish=current_time)
    connect.execute(command)
    connect.commit()