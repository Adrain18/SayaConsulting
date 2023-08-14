from flask import Blueprint, render_template, redirect, url_for
from models.type_of_material import TypeOfMaterial
from forms.type_of_material_forms import RegisterForm

material_views = Blueprint('material', __name__)

@material_views.route('/material/register/', methods=('GET', 'POST'))
def register():
    # Crea una instancia del formulario RegisterForm
    form = RegisterForm()

    if form.validate_on_submit():
        name_material = form.name_material.data
        price = form.price.data

        # Crea una instancia de Supplier con los datos del formulario
        typeofmaterial = TypeOfMaterial(name_material, price)

        # Guarda el proveedor en la base de datos utilizando el método save()
        typeofmaterial.save()

        return redirect(url_for('admin.tela'))

    return render_template('material/register.html', form=form)