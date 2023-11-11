from flask import request
from database.base import *


def ballans_prex(connect):
    args = request.json
    command = select(telegram_user).where(telegram_user.c.telegramId == args["userId"], telegram_user.c.isAdmin == True)
    result = connect.execute(command)
    if result.rowcount == 0:
        return {"success": False, "message": "Вы не являетесь администартором"}
    command = select(account).where(account.c.date_parish != "null")
    result = connect.execute(command)
    count_account = 0
    for i in result:
        count_account += 1
    valut: int = int(count_account) * 15000000
    ob_valut: int = int(count_account) * 65000000
    return {"success": True, "message": f"Общее количество валюты: {ob_valut}p ({ob_valut/1000000} млн р) ({ob_valut/1000000000} Млрд р)\nПрогназируемый процент: {valut}p ({valut/1000000} млн р) ({valut/1000000000} Млрд р)\nПрогназируемая прибыль: {valut/1000000 * 25.5}р\nПрибыль для выебонов: {ob_valut/1000000 * 200}р"}