from flask import Blueprint, render_template, redirect, url_for
from models.supplier import Supplier, Material
from forms.supplier_forms import RegisterForm

supplier_views = Blueprint('supplier', __name__)

@supplier_views.route('/supplier/register/', methods=('GET', 'POST'))
def register():
    # Crea una instancia del formulario RegisterForm
    form = RegisterForm()

    # Crea una instancia de Material
    material = Material()

    # Carga las opciones para el campo type_of_material
    type_of_materials = material.get_all()
    form.id_material.choices = [(m.id_material, m.name_material) for m in type_of_materials]

    if form.validate_on_submit():
        ape_mat = form.ape_mat.data
        ape_pat = form.ape_pat.data
        direction = form.direction.data
        id_material = form.id_material.data
        name = form.name.data

        # Crea una instancia de Supplier con los datos del formulario
        supplier = Supplier(ape_mat, ape_pat, direction, id_material, name)

        # Guarda el proveedor en la base de datos utilizando el método save()
        supplier.save()

        return redirect(url_for('admin.proveedor'))

    return render_template('supplier/register.html', form=form)