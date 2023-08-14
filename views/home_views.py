from flask import Blueprint, render_template, redirect, url_for, flash, abort, session
from models.users import User
from forms.user_forms import LoginForm

home_views = Blueprint('home', __name__)

@home_views.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        users = User.get_by_password(username, password)
        if not users:
            flash('Verifica tus Datos')
        else:
            session['user'] 
            #if users.id_role == 1:

            return render_template('home/inicio_sesion.html', user=user)
    return render_template('admin/sesion_admin.html', form=form)

#@home_views.route ('/logout/')
#def logout():
    