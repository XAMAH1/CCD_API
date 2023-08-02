from datetime import datetime
from datetime import timedelta
import threading
from time import sleep

from account.examination.history.examination_account_error import examination_account_error

def config_start_exam(connect):
    while True:
        now = datetime.now()
        run_at = now + timedelta(seconds=10)
        delay = (run_at - now).total_seconds()
        threading.Timer(delay, examination_account_error, args=(connect,)).start()
        sleep(10)