from flask import Flask, jsonify

app = Flask(__name__)


# Current weather for London
@app.route('/api/weather/current/london')
def current_weather_london():
    data = {
        "city": "London",
        "temperature": "18",
        "condition": "Cloudy",
        "humidity": "60%"
    }
    return jsonify(data)


# 3 days forecast for Paris
@app.route('/api/weather/forecast/paris')
def forecast_paris():
    forecast = [
        {"day": "Day 1", "temperature": "21°C", "condition": "Sunny"},
        {"day": "Day 2", "temperature": "19°C", "condition": "Cloudy"},
        {"day": "Day 3", "temperature": "17°C", "condition": "Rainy"}
    ]

    data = {
        "city": "Paris",
        "forecast_days": 3,
        "forecast": forecast
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
