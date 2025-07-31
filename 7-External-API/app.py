
from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/weather/lisboa")
def weather_lisboa():
    params = {
        'q': 'Lisboa,PT',
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        temp = data['main']['temp']
        
        return jsonify({
            'city':'Lisboa',
            'temperature_celsius':temp
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)