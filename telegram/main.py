from flask import request

from telegram.ballans.ballans import ballans
from telegram.ballans.ballans_prex import ballans_prex
from telegram.get_account.current_account import get_current_account_ccd
from telegram.get_account.get_account_ccd import get_account_ccd
from telegram.get_account.isAdmin_get import isAdmin_get
from telegram.telegram_new_user.telegram_new_user import telegram_new_user


def main_telegram(connect):
    if request.path == "/telegram/account/new":
        return telegram_new_user(connect)

    if request.path == "/telegram/ccd/account/get/info":
        return get_account_ccd(connect)

    if request.path == "/telegram/ccd/account/get":
        return get_current_account_ccd(connect)

    if request.path == "/telegram/ballans":
        return ballans(connect)

    if request.path == "/telegram/info/ballans/account":
        return ballans_prex(connect)

    if request.path == "/telegram/get/isAdmin":
        return isAdmin_get(connect)
