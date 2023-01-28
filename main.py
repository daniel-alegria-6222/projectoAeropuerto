from flask import Flask, render_template
from generic_airport import Fecha

import re
pattern = re.compile(r"\d\d-\d\d-\d\d\d\d")

app = Flask(__name__)

## create a route decorator
@app.route ( '/' )
def index():
    return render_template("index.html")


@app.route ( '/flight_board/<date>' )
def flight_board ( date:str ):
    if date == "today":
        date = str(Fecha.today())
    elif not pattern.match( date ):
        return "<h1>ROUTE ERROR:</h1>\n<p>You should access specific dates with the format 'dd-mm-yyyy'</p>"

    return render_template("flight_board.html", date=date)

@app.route ( '/users/' )
def users():
    return render_template("users.html")

@app.route ( '/operator/vuelos/' )
def op_vuelos ():
    "Muestra, modifica, filtra"
    return render_template("vuelos.html")

@app.route ( '/operator/' )
def op_index():
    return op_vuelos()

@app.route ( '/operator/operaciones_gerenciales/' )
def op_gerenciales():
    return render_template("op_gerenciales.html")
