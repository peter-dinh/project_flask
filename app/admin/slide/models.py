from app import db

class Slide(db.Model):

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String)
    image_name      = db.Column(db.String)
    image_link      = db.Column(db.String)
    link            = db.Column(db.String)
    info            = db.Column(db.String)
    sort_order      = db.Column(db.Integer)


    def __init__(self, name, image_name, image_link, link, info, sort_order):
        self.name       = name
        self.image_link = image_link
        self.image_name = image_name
        self.link       = link
        self.info       = info
        self.sort_order = sort_order

