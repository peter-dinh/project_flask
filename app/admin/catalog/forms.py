from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, SelectField
from flask_wtf.file import FileField

class Catalog_form(FlaskForm):

    name = TextField('name')
    parent_id = SelectField('parent_id')
    sort_order = SelectField('sort_order')
    submit = SubmitField("submit")