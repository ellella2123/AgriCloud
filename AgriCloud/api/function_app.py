import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def message(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        body=json.dumps({
            "city": "Success",
            "temp": 25,
            "advice": "The 500 error is fixed! Your Python 3.10 backend is live."
        }),
        mimetype="application/json",
        status_code=200
    )