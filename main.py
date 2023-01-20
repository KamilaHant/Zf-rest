# app.py
import json
from flask import Flask, request, jsonify
from typing import List, Dict
from users import User, Ledger

app = Flask(__name__)  # __name__ jmeno instance

ledger = Ledger()


ledger.add_user("Petr")
ledger.transaction("Pavel", "Petr", 15.0)
ledger.transaction("Petr", "Jakub", 2.5)


@app.get("/user/<name>/")  # get user by name
def get_user(name):
    user = ledger.get_user(name)
    return json.dumps(user.__dict__, indent=2)


@app.post("/add")  # add new user with name
def add_user():
    if request.is_json:  # chci aby pozadavek mel telo Json
        data = request.get_json()  # veme body a veme napsana data
        Ledger.add_user(data["user"])
        return 200
    return {"error": "Name is not unique or request has wrong format"}, 418


@app.post("/transaction")
def add_transaction():
    if request.is_json:
        data = request.get_json()
        Ledger.transaction(data["veritel"], data["dluznik"], data["castka"])
        return 200
    return {"error": "Request has wrong format"}, 418


app.run(host='0.0.0.0', port=81)
