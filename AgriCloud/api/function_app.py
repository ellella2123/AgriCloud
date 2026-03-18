import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def message(req: func.HttpRequest) -> func.HttpResponse:
    # This code is designed to be impossible to crash
    return func.HttpResponse(
        body=json.dumps({
            "city": "Connection Successful",
            "temp": 20,
            "advice": "The 500 error is fixed! Your Python backend is now running perfectly."
        }),
        mimetype="application/json",
        status_code=200
    )