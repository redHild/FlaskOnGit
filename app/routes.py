from app import app

@app_route("/")
@app_route("/index")
def index():
    return "Hello World!"



