from flask import Blueprint, render_template, redirect, url_for
from models.maquilero import Maquilero 
from forms.maquilero_forms import RegisterForm

maquilero_views = Blueprint('maquilero', __name__)

@maquilero_views.route('/maquilero/register/', methods=('GET', 'POST'))
def register():
    # Crea una instancia del formulario RegisterForm
    form = RegisterForm()

    if form.validate_on_submit():
        ape_mat = form.ape_mat.data
        ape_pat = form.ape_pat.data
        direction = form.direction.data
        name = form.name.data

        # Crea una instancia de Supplier con los datos del formulario
        maquilero = Maquilero(ape_mat, ape_pat, direction, name)

        # Guarda el proveedor en la base de datos utilizando el método save()
        maquilero.save()

        return redirect(url_for('admin.maquilero'))

    return render_template('maquilero/register.html', form=form)