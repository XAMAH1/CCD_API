from database.base import *
import datetime
from examination.examination.check_time.time_check import time_check_error

def examination_account_error(connect):
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    command = select(history_account).where(history_account.c.date_parish == current_date, history_account.c.success == "В процессе")
    result = connect.execute(command)
    for i in result:
        time_check_error(connect, i)
    #   print("-" * 30)