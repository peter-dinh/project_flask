from flask import Blueprint, render_template, redirect, request, url_for, session, flash, abort
import hashlib

from app.admin.admin.models import Admin

from app import db

mod_admin = Blueprint('admin', __name__, url_prefix='/admin/admin')

@mod_admin.route('/')
def index():
    list_admin = Admin.query.order_by(Admin.id)
    return render_template('admin/admin/index.html', list = list_admin)
    
@mod_admin.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        email = request.form['email']
        if Admin.query.filter_by(email = email).first():
            flash("Email exists in system", "error")
            return redirect(url_for('.add'))
        password = hashlib.md5(request.form['password']).hexdigest()
        name = request.form['name']
        user = Admin(email, password, name)
        db.session.add(user)
        db.session.commit()
        flash('You add success!', 'success')
        return redirect(url_for('.index'))
    return render_template('admin/admin/add.html')
    
@mod_admin.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    if not Admin.query.filter_by(id = id).first():
        flash("ID account doesn't exists", "error")
        return  redirect(url_for('.index'))

    user = Admin.query.filter_by(id = id).first()

    if request.method == "POST":
        user.email = request.form['email']
        if request.form['password'] != '':
            user.password = hashlib.md5(request.form['password']).hexdigest()
        user.name = request.form['name']
        db.session.commit()
        flash("Edit account success!", "success")
        return redirect(url_for('.index'))

    return render_template('admin/admin/edit.html', user = user)
    
@mod_admin.route('/delete/<id>')
def delete(id):
    if not Admin.query.filter_by(id = id).first():
        flash("ID account doesn't extsts","error")
        return redirect(url_for('.index'))
    Admin.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Delete account success!", 'success')
    return redirect(url_for('.index'))