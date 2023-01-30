from flask import Flask, render_template, flash, redirect

# para la creacion de 'forms'
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
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

class BookForm(FlaskForm):
    validators = [DataRequired()]
    dni        = StringField("ID", validators=validators)
    nroVuelo   = StringField("Nro. Vuelo", validators=validators)
    submit = SubmitField("Submit") 

class VueloForm(FlaskForm):
    validators = [DataRequired()]
    nroVuelo   = StringField("Nro. Vuelo", validators=validators)
    aerolinea  = StringField("Aerolinea", validators=validators)
    avion      = StringField("Avion", validators=validators)
    fecha      = StringField("Fecha (dd-mm-yyyy)", validators=validators)
    hora       = StringField("Hora", validators=validators)
    estado     = SelectField("estado", choices=ga.Vuelo.ESTADOS, validators=validators)
    destino    = StringField("Destino", validators=validators)
    origen     = StringField("Origen", validators=validators)
    submit     = SubmitField("Submit") 

class AvionForm(FlaskForm):
    validators = [DataRequired()]
    codigo              = StringField("Codigo", validators=validators)
    autonomiaDeVueloKM  = StringField("Autonomia de Vuelo (KM)", validators=validators)
    altura              = StringField("Altura", validators=validators)
    longitudAla         = StringField("Longitud de Ala", validators=validators)
    capacidadToneladas  = StringField("Capacidad (Toneladas)", validators=validators)
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
    vuelos = org.getVuelosByFecha( ga.Fecha.newFromStr(date) )
    return render_template("flight_board.html", date=date, vuelos=vuelos)

@app.route ( '/user/', methods=['GET', 'POST'] )
def user():
    form = UserForm()
    if form.validate_on_submit():
        success = org.incluirUsuario(
            ga.Usuario(
                form.nombreCompleto.data,
                form.telefono.data,
                form.email.data,
                form.dni.data,
                ga.Fecha.newFromStr(form.fechaNacimiento.data),
            )
        )
        if success:
            flash("Added user successfully")
        else:
            flash("Couldn't add user")

    return render_template("user.html", form=form)

@app.route ( '/book/', methods=['GET', 'POST'] )
def book():
    form = BookForm()
    if form.validate_on_submit():
        nroVuelo = str(form.nroVuelo.data).strip(" ")
        ok = True

        if nroVuelo.isdigit():
            if not org.getVueloByNro( nroVuelo ):
                flash("Error: nroVuelo no existe")
                ok = False
        elif nroVuelo != "":
            flash("Error: nroVuelo no es un digito")
            ok = False
        else:
            nroVuelo = None


        # flash("Error: nroVuelo no es un digito")
        # flash("Error: nroVuelo no existe")

        if ok :
            pass
            # success = org.( form.dni.data, nroVuelo )
            # if success:
            #     flash("Added user successfully")
            # else:
            #     flash("Couldn't add user")

    return render_template("book.html", form=form)


## OPERATOR ROUTES
@app.route ( '/operator/vuelos/', methods=['GET', 'POST'] )
def op_vuelos ():
    # Muestra, modifica, filtra
    form = VueloForm()
    if form.validate_on_submit():
        vuelo = ga.Vuelo(
                form.nroVuelo.data,
                form.aerolinea.data,
                form.avion.data,
                ga.Fecha.newFromStr(form.fecha.data),
                form.hora.data,
                form.estado.data,
                form.destino.data,
                form.origen.data,
                # form.pasajeros.data,
            )
        success = org.incluirVuelo(vuelo)
        if success:
            flash("Added flight successfully")
        else:
            flash("Couldn't add flight")

    return render_template("op_vuelos.html", vuelos=org.vuelos, form=form) 

@app.route ( '/operator/' )
def op_index():
    return op_vuelos()

@app.route ( '/operator/aviones/', methods=['GET', 'POST']  )
def op_aviones():
    # Muestra, modifica, filtra
    form = AvionForm()
    if form.validate_on_submit():
        avion = ga.Avion(
                form.codigo.data,
                form.autonomiaDeVueloKM.data,
                form.altura.data,
                form.longitudAla.data,
                form.capacidadToneladas.data,
            )
        success = org.incluirAvion(avion)
        if success:
            flash("Added Airplane successfully")
        else:
            flash("Couldn't add airplane")

    return render_template("op_aviones.html", aviones=org.aviones, form=form) 

@app.route ( '/operator/operaciones_gerenciales/' )
def op_gerenciales():
    return render_template("op_gerenciales.html")

@app.route ( '/operator/users/' )
def op_users():
    # Muestra, modifica, filtra
    return render_template("op_users.html", usuarios=org.usuarios )


### UPDATE OPERATOR ROUTES
@app.route ( '/operator/vuelo_update/<int:id>', methods=['GET', 'POST']  )
def op_vuelo_update(id):
    ant_vuelo = org.getVueloByNro(id)
    form = VueloForm()

    if form.validate_on_submit():

        vuelo = ga.Vuelo(
                form.nroVuelo.data,
                form.aerolinea.data,
                form.avion.data,
                ga.Fecha.newFromStr(form.fecha.data),
                form.hora.data,
                form.estado.data,
                form.destino.data,
                form.origen.data,
                # form.pasajeros.data,
            )
        success = org.updateVuelo( ant_vuelo, vuelo )

        if success:
            return redirect( "/operator/vuelos" )
        else:
            flash("Couldn't update flight")

    return render_template("op_vuelo_update.html", ant_vuelo=ant_vuelo, form=form)

@app.route ( '/operator/vuelo_delete/<int:id>' )
def op_vuelo_delete(id):
    org.deleteVuelo(id)
    return redirect( "/operator/vuelos" )

### EXTRA
@app.route ( '/operator/save/' )
def op_save():
    # Muestra, modifica, filtra
    org.guardarDatos()
    return "<h1> Saved Successfully </h1>"
