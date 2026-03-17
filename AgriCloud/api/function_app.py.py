import azure.functions as func
import json
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message")
def message(req: func.HttpRequest) -> func.HttpResponse:
    city = req.params.get('city')
    
    # --- TEST MODE: If you don't have an API key yet ---
    if not city:
        return func.HttpResponse("Please enter a city", status_code=400)

    # Use a real key if you have one, otherwise this is a "Demo" response
    api_key = "b2b8945ab53a56945813d94fa379ed13" 
    
    if api_key == "b2b8945ab53a56945813d94fa379ed13":
        # This part runs if you haven't put a real key in yet
        return func.HttpResponse(
            json.dumps({
                "city": city,
                "temp": 295, # Fake data (22°C)
                "advice": "Demo Mode: The sun is shining! Good for planting maize."
            }),
            mimetype="application/json"
        )
    
    # If you HAVE a key, this part runs:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        r = requests.get(url)
        data = r.json()
        return func.HttpResponse(json.dumps({
            "city": city,
            "temp": data['main']['temp'],
            "advice": "Real-time data: Watch the clouds!"
        }), mimetype="application/json")
    except:
        return func.HttpResponse("Error connecting to weather service", status_code=500)