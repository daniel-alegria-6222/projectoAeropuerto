from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import re

import generic_airport as ga
from generic_airport import Organizador


date_pattern = re.compile(r"\d\d-\d\d-\d\d\d\d")
org = ga.Organizador()

app = Flask(__name__)
app.config["SECRET_KEY"] = "no importa ahora"


import os
def out( value ):
    os.system(f"echo '{str(value)}'>> out.txt")

## Create a form class
class UserForm(FlaskForm):
    validators = [DataRequired()]
    nombreCompleto  = StringField("Name", validators=validators)
    telefono        = StringField("Phone number", validators=validators)
    email           = StringField("Email", validators=validators)
    dni             = StringField("ID", validators=validators)
    fechaNacimiento = StringField("Birthdate (dd-mm-yyyy)", validators=validators)
    submit     = SubmitField("Submit") 


###
## ROUTES
@app.route ( '/' )
def index():
    return render_template("index.html")

@app.route ( '/flight_board/<date>' )
def flight_board ( date:str ):
    if date == "today":
        date = str(ga.Fecha.today())
    elif not date_pattern.match( date ):
        return "<h1>ROUTE ERROR:</h1>\n<p>You should access specific dates with the format 'dd-mm-yyyy'</p>"

    return render_template("flight_board.html", date=date)

@app.route ( '/user/', methods=['GET', 'POST'] )
def user():
    form = UserForm()
    if form.validate_on_submit():
        org.usuarios.append(
            ga.Pasajero(
                form.nombreCompleto.data,
                form.telefono.data,
                form.email.data,
                form.dni.data,
                form.fechaNacimiento.data,
            )
        )

    return render_template("user.html", form=form)


## OPERATOR ROUTES
@app.route ( '/operator/vuelos/' )
def op_vuelos ():
    # Muestra, modifica, filtra
    return render_template("op_vuelos.html")

@app.route ( '/operator/' )
def op_index():
    return op_vuelos()

@app.route ( '/operator/operaciones_gerenciales/' )
def op_gerenciales():
    return render_template("op_gerenciales.html")

@app.route ( '/operator/users/' )
def op_users():
    # Muestra, modifica, filtra
    return render_template("op_users.html", usuarios=org.usuarios )
