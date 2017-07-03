from flask import Blueprint, render_template, request, redirect, session, abort

from app.admin.catalog.models import Catalog

mod_catalog = Blueprint( 'catalog', __name__, "/admin/catalog" )

mod_catalog.route('/'):
def index():
    catalog = Catalog.query.all()
    return render_template('./admin/catalog/index.html', catalog = catalog)

mod_catalog.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        parent_id = request.form['parent_id']
        sort_order = request.form['sort_order']
        catalog = Catalog(name, parent_id, sort_order)
        db.session.add(catalog)
        db.session.commit()
        flash('Add catalog succeess!', 'success')
        return redirect('./index')
    return render_template('./admin/catalog/add.html')

mod_catalog.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    catalog_info = Catalog.query.filter_by(id= id).first()
    if not catalog_info:
        flash("ID Catalog doesn't exists", "error")
    if request.method == 'POST':
        catalog_info.name = request.form['name']
        catalog_info.parent_id = request.form['parent_id']
        catalog_info.sort_order = request.form['sort_order']
        db.session.commit()
