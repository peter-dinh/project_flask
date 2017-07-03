from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import validators
from wtforms import TextField, PasswordField, SubmitField


class Login(FlaskForm):
    email     = TextField("email", [validators.Required("Please enter email.")])
    password  = PasswordField("password")
    submit    = SubmitField("login")

