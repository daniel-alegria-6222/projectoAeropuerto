## About

Repositorio para un projecto dejado en el curso de 'PROGRAMACION I', enero 2023

#### Integrantes
- Alegria Sallo Daniel Rodrigo  (215270)
- Conde Sallo Mihail Johan      (215783)
- Sotelo Quispe Julio Cesar     (215791)

## Como correr el codigo?

Instalar los requerimientos:

    pip install -r requirements.txt

En el directorio del projecto, correr el server local:

    python -m flask --app=main.py --debug run


## Modo de uso
Abrir los links principales del server y se veran varias funciones:

http://127.0.0.1:5000/

http://127.0.0.1:5000/operator



Tambien se puede ver informacion y vuelos de un usuario con:

http://127.0.0.1:5000/user/${DNI}


Ademas de actualizar y eliminar un usuario con:

http://127.0.0.1:5000/user/update/${DNI}

http://127.0.0.1:5000/user/delete/${DNI}
