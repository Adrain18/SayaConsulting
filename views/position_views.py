from flask import Blueprint, render_template, redirect, url_for
from models.positions import Position 
from forms.position_forms import RegisterForm

position_views = Blueprint('position', __name__)

@position_views.route('/position/register/', methods=('GET', 'POST'))
def register():
    # Crea una instancia del formulario RegisterForm
    form = RegisterForm()

    if form.validate_on_submit():
        name_position = form.name_position.data
        machinery_in_use = form.machinery_in_use.data

        # Crea una instancia de Supplier con los datos del formulario
        position = Position(name_position, machinery_in_use)

        # Guarda el proveedor en la base de datos utilizando el método save()
        position.save()

        return redirect(url_for('admin.puestos'))

    return render_template('position/register.html', form=form)