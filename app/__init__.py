from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config.from_object("config")
app.debug =True

db = SQLAlchemy(app)



from app.demo.controllers import mod_demo
app.register_blueprint(mod_demo)






# register controllers admin
from app.admin.login.controllers import mod_admin_login
app.register_blueprint(mod_admin_login)

from app.admin.admin.controllers import mod_admin
app.register_blueprint(mod_admin)