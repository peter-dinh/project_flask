from flask import Blueprint, request, render_template, redirect, session, flash, url_for, abort
import hashlib

from app.admin.login.forms import Login
from app.admin.admin.models import Admin



mod_admin_login = Blueprint('admin_login', __name__, url_prefix='/admin')

@mod_admin_login.route('/', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('.dashboard'))
    form = Login()
    if request.method == "POST":
        email = request.form['email']
        password = hashlib.md5(request.form['password']).hexdigest()
        if Admin.query.filter_by(email = email, password = password).first():
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('.dashboard'))
    return render_template('admin/login/index.html', form=form)

@mod_admin_login.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        abort(401)
    else:
        user = session['logged_in']
        return render_template('admin/dashboard/index.html', user=user)
        
@mod_admin_login.route('/logged_out')
def logged_out():
    session.pop('logged_in', None)
    return redirect(url_for('.login'))