from flask import Blueprint, session, request, redirect, url_for, abort, render_template, flash

import os

from app.admin.slide.models import Slide

from app import db


mod_slide = Blueprint('slide', __name__, url_prefix='/admin/slide')

@mod_slide.route('/')
def index():
    slide = Slide.query.order_by(Slide.sort_order)
    return render_template('admin/slide/index.html', slide = slide)

@mod_slide.route('/add', methods=['GET', 'POST'])
def add():


    if request.method == 'POST':
        name        = request.form['name']
        image_name  = request.form['image_name']
        file  = request.files['image_link']
        image_link = file.filename
        link        = request.form['link']
        info        = request.form['info']
        sort_order  = request.form['sort_order']
        slide = Slide(name, image_name, image_link, link, info,sort_order)
        db.session.add(slide)
        db.session.commit()
        flash('Add slide success!', 'success')
        return redirect(url_for('.index'))
    return render_template('admin/slide/add.html')

@mod_slide.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):

    slide_info = Slide.query.filter_by(id=id).first()
    if not slide_info:
        flash("ID slide doesn't exists", "error")
        return redirect(url_for('.index'))
    if request.method == 'POST':
        slide_info.name = request.form['name']
        if request.files['image_link']:
            file = request.form['image_link']
            slide_info.image_link = file.filename
        slide_info.link = request.form['link']
        slide_info.info = request.form['info']
        slide_info.sort_order = request.form['sort_order']
        db.session.commit()
        flash('Edit slide success!', 'success')
        return redirect(url_for('.index'))
    return render_template('admin/slide/eidt.html', slide_info = slide_info)

@mod_slide.route('/delete/<id>')
def delete(id):

    if not Slide.query.filter_by(id = id).first():
        flash("ID slide doesn't exists", "error")
        return redirect(url_for('.index'))
    Slide.query.filter_by(id = id).delete()
    flash('Delete slide success!', 'success')
    return redirect(url_for('.index'))

