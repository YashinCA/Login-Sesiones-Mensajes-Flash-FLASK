# importo desde utils
from utils import lg
from flask import Flask, render_template, request, redirect, session, flash
# 4. importo el archivo configuraciones
from settings import Config
# Crea una nueva instancia de la clase Flask llamada "app"
app = Flask(__name__)
# 1. para evitar subir arvhivos importantes a GIT, haremos un
# arechivo configuraciones.py y un gitignore para indicar que archivo no debe considerar.
# le indicamos a configuracion los secret keys
# 5. indico que mi clave secreta la saque de Config.SECRET_KEY
app.secret_key = Config.SECRET_KEY
# 6. hacer un README.md para indicarle a otra persona lo que debe configurar


@app.route('/')
def index():
    return redirect('/inicio')


@app.route('/inicio')
def inicio():
    if 'usuario' not in session:
        flash('No estás logeado. Debes ingresar tu contraseña')
        return redirect('/login')
    return render_template('inicio.html')


@app.route('/login')
def login():
    if 'usuario' in session:
        flash('Ya estas Logeado. Para salir debes ir al boton salir', 'error')
        return redirect('/inicio')
    return render_template('login.html')


@app.route('/login_procesar', methods=['POST'])
def login_procesar():
    # SIEMPRE SIEMPRE AGREGAR EL REQUEST.FORM
    # Por seguridad creamos la carpeta utils y asi no mostrar
    # los post de usuario y contraseña
    lg("POST:", request.form)
    lg(request.form['tipo'])
    if ((request.form['password'] != '1234') or (request.form['tipo'] != 'login')):
        # agregamos este mensaje flash para que lo vea el usuario
        # DEBEMOS HACER QUE SE LEA DESDE EL MISMO TEMPLATE
        flash('Contraseña incorrecta', 'error')
        print('no logueado')
        return redirect("/login")

    print('si logueado')
    session['usuario'] = request.form['email']
    flash('Logeado Correctamente.', 'success')
    return redirect('/inicio')


@app.route('/logout')
def logout():
    # si el usuario esta en sesion
    if 'usuario' in session:
        session.pop('usuario')
    return redirect('/login')


if __name__ == "__main__":
    # podemos cambiar el puerto si quisieramos
    app.run(debug=Config.DEBUG, port=Config.PORT)
