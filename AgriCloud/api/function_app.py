import azure.functions as func
import json

# Setting the global auth level to ANONYMOUS
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def message(req: func.HttpRequest) -> func.HttpResponse:
    # Get city from the web request
    city = req.params.get('city')
    
    # This is a test response to confirm the 403 error is fixed
    return func.HttpResponse(
        json.dumps({
            "city": city if city else "Unknown",
            "temp": 298,
            "advice": "The 403 error is gone! Welcome to AgriCloud Smart Dashboard."
        }),
        mimetype="application/json"
    )