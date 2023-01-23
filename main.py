# app.py

import json
import logging
import logging.handlers
import initialize
from flask import Flask, request, jsonify
from users import Ledger

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

app = Flask(__name__)  # __name__ jmeno instance

ledger = Ledger()

initialize.initialize_data(ledger)

@app.get("/user/<name>/")
def get_user(name):
    user = ledger.get_user(name)
    return json.dumps(user.__dict__, indent=2)


@app.post("/add")
def add_user():
    if request.is_json:
        data = request.get_json()
        ledger.add_user(data["user"])
        return json.dumps(ledger.get_user(data["user"]).__dict__)
    return {"error": "Name is not unique or request has wrong format"}


@app.post("/transaction")
def add_transaction():
    if request.is_json:
        data = request.get_json()
        ledger.transaction(
            data["veritel"], data["dluznik"], float(data["castka"]))
        return json.dumps({
            "users": [
                ledger.get_user(data["veritel"]).__dict__,
                ledger.get_user(data["dluznik"]).__dict__
            ]
        })
    return {"error": "Request has wrong format"}


app.run(host='0.0.0.0', port=81)
