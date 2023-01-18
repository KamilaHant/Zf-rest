# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "petr": {"pavel": 15, "jiri": 1, "dan": 4.5},
    "jakub": {"petr": 15, "jiri": 1, "dan": 4.5},
    "pavel": {"petr": 15, "jiri": 1, "dan": 4.5},
    "dan": {"pavel": 15, "jiri": 1, "jakub": 4.5}

}


def _find_next_id():
    return max(country["id"] for country in countries) + 1


@app.get("/countries")
def get_countries():
    return jsonify(countries)


@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


app.run(host='0.0.0.0', port=81)