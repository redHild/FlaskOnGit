from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Praise Lord Honk, the bringer of Chaos and Death'}
    return render_template('index.html', title='Home', user=user)
