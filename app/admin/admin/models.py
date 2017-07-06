from app import db

class Admin(db.Model):
    
    id             = db.Column(db.Integer, primary_key=True)
    email          = db.Column(db.String, unique=True)
    password       = db.Column(db.String)
    name           = db.Column(db.String)
    group_admin    = db.Column(db.Integer)
    
    def __init__(self, email, password, name, group_admin=0):
        self.email       = email
        self.password    = password
        self.name        = name
        self.group_admin = group_admin