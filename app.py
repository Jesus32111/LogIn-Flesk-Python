from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DB_FILE = 'users.json'

# Cargar usuarios desde JSON
def cargar_usuarios():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as archivo:
        datos = json.load(archivo)
    return datos.get('usuarios', [])

# Guardar usuarios en JSON
def guardar_usuario(username, password):
    usuarios = cargar_usuarios()
    usuarios.append({'username': username, 'password': password})
    with open(DB_FILE, 'w') as archivo:
        json.dump({'usuarios': usuarios}, archivo, indent=4)

# Página de login
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

# Página de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    mensaje = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuarios = cargar_usuarios()
        if any(u['username'] == username for u in usuarios):
            mensaje = 'El usuario ya existe'
        else:
            guardar_usuario(username, password)
            return redirect(url_for('login'))
    return render_template('registro.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
