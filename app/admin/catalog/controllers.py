from flask import Blueprint, render_template, request, url_for, flash, redirect, session, abort

from app.admin.catalog.models import Catalog

from app.admin.catalog.models import Catalog as X

from app import db

mod_catalog = Blueprint( 'catalog', __name__, url_prefix="/admin/catalog" )

@mod_catalog.route('/', methods=['GET'])
def index():

    catalog = Catalog.query.order_by(Catalog.parent_id)
    list_parent = Catalog.query.filter_by(parent_id = 0).all()
    k = {item.id: item.name for item in list_parent}

    return render_template('./admin/catalog/index.html', catalog = catalog, list_parent = k)

@mod_catalog.route('/add', methods=['GET', 'POST'])
def add():
    list_parent = Catalog.query.filter_by(parent_id = 0).all()
    
    if request.method == 'POST':
        name = request.form['name']
        parent_id = request.form['parent_id']
        sort_order = request.form['sort_order']
        catalog = Catalog(name, parent_id, sort_order)
        db.session.add(catalog)
        db.session.commit()
        flash('Add catalog succeess!', 'success')
        return redirect(url_for('.index'))
    return render_template('./admin/catalog/add.html', list_parent = list_parent)

@mod_catalog.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    catalog_parent = Catalog.query.filter_by(parent_id = 0).all()
    catalog_info = Catalog.query.filter_by(id= id).first()
    if not catalog_info:
        flash("ID Catalog doesn't exists", "error")
        redirect(url_for('.index'))
    if request.method == 'POST':
        catalog_info.name = request.form['name']
        catalog_info.parent_id = request.form['parent_id']
        catalog_info.sort_order = request.form['sort_order']
        db.session.commit()
        flash('Edit catalog success!', 'success')
        return redirect(url_for('.index'))
    return render_template('./admin/catalog/edit.html',  catalog_info = catalog_info, catalog_parent = catalog_parent)

@mod_catalog.route('/delete/<id>')
def delete(id):
    if not Catalog.query.filter_by(id = id).first():
        flash("ID Catalog doesn't exists", "error")
        return redirect(url_for('.index'))
    Catalog.query.filter_by(id = id).delete()
    db.session.commit()
    flash("Delete catalog success!", "success")
    return redirect(url_for('.index'))