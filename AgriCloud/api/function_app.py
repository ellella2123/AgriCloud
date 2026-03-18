import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def message(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    return func.HttpResponse(
        body=json.dumps({
            "city": "System Online",
            "temp": 20,
            "advice": "The 500 error is gone. Python 3.11 is now powering AgriCloud!"
        }),
        mimetype="application/json",
        status_code=200
    )