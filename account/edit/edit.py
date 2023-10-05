from database.base import *
from flask import request

def edit(connect):
    args = request.args
    command = update(history_account).values({"success": args["message"]}).where(history_account.c.id == args["id"])
    connect.execute(command)
    connect.commit()
    return {"success": True, "message": f"account status update {args['id']}"}