import azure.functions as func
import requests
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    city = req.params.get('city')
    
    # 1. Get Weather
    # Replace 'YOUR_KEY' with a key from openweathermap.org (it's free)
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_KEY"
    weather_data = requests.get(weather_url).json()
    
    # 2. Logic: If weather is 'Rain', suggest planting
    suggestion = "Good day for irrigation"
    if "Rain" in weather_data['weather'][0]['main']:
        suggestion = "Collect rainwater today!"

    return func.HttpResponse(
        json.dumps({
            "city": city,
            "temp": weather_data['main']['temp'],
            "advice": suggestion
        }),
        mimetype="application/json"
    )