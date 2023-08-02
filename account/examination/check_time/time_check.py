from database.base import *
from datetime import datetime
from datetime import timedelta

def time_check_error(connect, current_account):
    now = datetime.now()
    nowtime = datetime(int(current_account[4].split(".")[2]), int(current_account[4].split(".")[1]), int(current_account[4].split(".")[0]), int(current_account[5].split(":")[0]), int(current_account[5].split(":")[1]), int(current_account[5].split(":")[2]))
    run_at = nowtime + timedelta(minutes=15)
    if now > nowtime:
        print(f'{run_at}\t{nowtime}\t UPDATE')
    else:
        print(f'{run_at}\t{nowtime}\t NO UPDATE')