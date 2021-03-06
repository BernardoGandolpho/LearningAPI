from flask import Flask, request, jsonify

# Creating Flask app
app = Flask(__name__)

# List of dictionaries to replace a database
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]


# Funtion to find the next id for POST requests
def _find_next_id():
    return max(country["id"] for country in countries) + 1


# Routes
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