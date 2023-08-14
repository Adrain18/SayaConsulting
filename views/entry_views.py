from flask import Blueprint, render_template

entry_views = Blueprint('entry', __name__)

@entry_views.route('/entrada_material/')
def entrada_material():
    return render_template('entry/entrada_material.html')

@entry_views.route('/producto_entregar/')
def producto_entregar():
    return render_template('entry/producto_entregar.html')

@entry_views.route('/producto_procesar/')
def producto_procesar():
    return render_template('entry/producto_procesar.html')
