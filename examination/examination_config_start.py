from datetime import datetime
from datetime import timedelta
import threading
from time import sleep

from examination.examination.history.examination_account_error import examination_account_error
from database.base import *

def config_start_exam():
    connect2 = base_connect()
    while True:
        now = datetime.now()
        run_at = now + timedelta(seconds=3)
        delay = (run_at - now).total_seconds()
        threading.Timer(delay, examination_account_error, args=(connect2,)).start()
        sleep(3)