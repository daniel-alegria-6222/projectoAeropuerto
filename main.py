from flask import Flask, render_template

app = Flask(__name__)

## create a route decorator
@app.route ( '/' )
def index():
    return render_template("index.html")


@app.route ( '/flight_board/' )
def flight_board():
    return render_template("flight_board.html")


@app.route ( '/users/' )
def users():
    return render_template("users.html")
