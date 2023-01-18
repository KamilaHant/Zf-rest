# app.py
from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)

users = {
    "jmeno": str,
    "dluzi": List[Dict[str, float]],
    "dluzi_mu": List[Dict[str,float]],
    "suma": float
}


@app.get("/users")
def get_user():
    return jsonify(users)


@app.post("/users")
def add_user():
    if request.is_json:
        user = request.get_json()
        user["jmeno"] = _find_next_id()
        users.append(user)
        return user, 201
    return {"error": "Request must be JSON"}, 415


app.run(host='0.0.0.0', port=81)