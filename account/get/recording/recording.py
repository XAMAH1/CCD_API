from database.base import *
from flask import request
import datetime
def record(connect, login, id, type_operation):
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    current_time = now.strftime("%H:%M:%S")
    command = insert(history_account).values(login=login, id_user=id, date_parish=current_date, time_parish=current_time, type_operation=type_operation)
    connect.execute(command)
    connect.commit()
    command = select(history_account).where(history_account.c.id_user == str(id), history_account.c.login == str(login), history_account.c.date_parish == current_date, history_account.c.time_parish == current_time)
    result = connect.execute(command)
    for i in result:
        return i[0]