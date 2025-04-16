from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def cargar_usuarios():
    with open('users.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos['usuarios']

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuarios = cargar_usuarios()
        for usuario in usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                return f"<h1>¡Bienvenido, {username}!</h1>"
        mensaje = 'Usuario o contraseña incorrectos'
    return render_template('login.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
