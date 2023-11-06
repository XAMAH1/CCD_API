from datetime import datetime

from database.base import *

def account_remain(connect):
    current_date = datetime.now().strftime("%d.%m.%Y")
    command = select(account).where(account.c.date_parish != null)
    result = connect.execute(command)
    count_account = 0
    for i in result:
        count_account += 1
    command = select(history_account).where(history_account.c.date_parish == current_date, history_account.c.success == "Выполнено")
    result = connect.execute(command)
    count_account_completed = 0
    for i in result:
        count_account_completed += 1
    return {"success": True, "message": f"Аккаунов всего {count_account}\nПройдено аккаунтов {count_account_completed}\nОсталось {count_account - count_account_completed}"}
