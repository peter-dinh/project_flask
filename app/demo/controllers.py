from flask import Blueprint, request, redirect, render_template

mod_demo = Blueprint('demo', __name__, url_prefix='/demo')

@mod_demo.route('/')
def index():
    return render_template('demo/index.html')