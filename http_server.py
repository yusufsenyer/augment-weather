from flask import Flask, jsonify, request
from app import get_current_weather_by_city, get_current_weather_by_coordinates
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Weather API Server",
        "endpoints": {
            "/weather/city/<city_name>": "Get weather by city name",
            "/weather/coords/<lat>/<lon>": "Get weather by coordinates"
        }
    })

@app.route('/weather/city/<city_name>')
def weather_by_city(city_name):
    try:
        weather_data = get_current_weather_by_city(city_name)
        return jsonify({
            "success": True,
            "data": weather_data
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/weather/coords/<float:lat>/<float:lon>')
def weather_by_coords(lat, lon):
    try:
        weather_data = get_current_weather_by_coordinates(lat, lon)
        return jsonify({
            "success": True,
            "data": weather_data
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
