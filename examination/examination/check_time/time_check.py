from database.base import *
from datetime import datetime
from datetime import timedelta

def time_check_error(connect, current_account):
    now = datetime.now()
    nowtime = datetime(int(current_account[4].split(".")[2]), int(current_account[4].split(".")[1]), int(current_account[4].split(".")[0]), int(current_account[5].split(":")[0]), int(current_account[5].split(":")[1]), int(current_account[5].split(":")[2]))
    run_at = nowtime + timedelta(minutes=20)
    if now > run_at:
        command = update(history_account).values({"success": "Ошибка. Время на выполнение закончилось", "date_expiration": run_at}).where(history_account.c.id == current_account[0])
        connect.execute(command)
        connect.commit()
        print(f'{run_at}\t{nowtime}\t UPDATE')
    else:
        print(f'{run_at}\t{nowtime}\t NO UPDATE')