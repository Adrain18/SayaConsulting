from flask import Blueprint, render_template, redirect, url_for
from models.product import Product, Material
from forms.product_forms import RegisterForm

product_views = Blueprint('product', __name__)

@product_views.route('/product/register/', methods=('GET', 'POST'))
def register():
    # Crea una instancia del formulario RegisterForm
    form = RegisterForm()

    # Crea una instancia de Material
    material = Material()

    # Carga las opciones para el campo type_of_material
    type_of_materials = material.get_all()
    form.id_material.choices = [(m.id_material, m.name_material) for m in type_of_materials]

    if form.validate_on_submit():
        name_product = form.name_product.data
        id_material = form.id_material.data
        size = form.size.data
        price = form.price.data

        # Crea una instancia de Supplier con los datos del formulario
        product = Product(name_product, id_material, size, price)

        # Guarda el proveedor en la base de datos utilizando el método save()
        product.save()

        return redirect(url_for('admin.producto'))

    return render_template('product/register.html', form=form)