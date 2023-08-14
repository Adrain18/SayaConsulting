from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from controller.UserController import *
from werkzeug.security import generate_password_hash
from config import config
from views.admin_views import admin_views
from views.user_views import user_views
# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)
app.register_blueprint(admin_views)
app.register_blueprint(user_views)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('inicio'))
            else:
                flash("Contraseña invalida")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/inicio')
@login_required
def inicio():
    return render_template('admin/inicio.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


@app.route('/usuario')
def usuario():
    return render_template('admin/usuario.html')


@app.route('/registrar-user', methods=['GET','POST'])
def addUser():
    return render_template('users/register.html')

#Registrando nuevo carro
@app.route('/usuario', methods=['POST'])
def formAddUser():
    if request.method == 'POST':
        username            = request.form['username']
        password            = request.form['password']
        fullname            = request.form['fullname']
        
        password = generate_password_hash(password)
        resultData = registrarUser(username, password, fullname)
        if(resultData ==1):
             return render_template('admin/usuario.html', miData = listaUser(), msg='El Registro fue un éxito', tipo=1)
        else:
            return render_template('admin/usuario.html', msg = 'Metodo HTTP incorrecto', tipo=1)   



@app.route('/usuario/<string:id>/update', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateUser(id)
        if resultData:
            return render_template('users/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaUser(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaUser(), msg = 'Metodo HTTP incorrecto', tipo=1)          


@app.route('/actualizar-usuario/<string:idUser>', methods=['POST'])
def  formActualizarUser(idUser):
    if request.method == 'POST':
        username     = request.form['username']
        password     = request.form['password']
        fullname     = request.form['fullname']
       
        resultData = recibeActualizarUser(username, password, fullname,idUser)

        if(resultData ==1):
            return render_template('admin/usuario.html', miData = listaUser(), msg='Datos del carro actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('admin/usuario.html', miData = listaUser(), msg='No se pudo actualizar', tipo=1)


@app.route('/borrar-usuario/<string:id>', methods=['GET','POST'])
def formViewBorrarUsuario(id):
    if request.method == 'GET':
        resultData  = eliminarUser(id)
    
        if(resultData ==1):
            return render_template('admin/usuario.html', miData = listaUser(), msg='Registro borrado con exito', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('admin/usuario.html', miData = listaUser(), msg='No se pudo actualizar', tipo=1)

        




if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()