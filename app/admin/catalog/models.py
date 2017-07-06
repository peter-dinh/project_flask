from app import db


class Catalog(db.Model):

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String)
    parent_id  = db.Column(db.Integer)
    sort_order = db.Column(db.Integer)

    def __init__(self, name, parent_id, sort_order):
        self.name          = name
        self.parent_id     = parent_id
        self.sort_order    = sort_order