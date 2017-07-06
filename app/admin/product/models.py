from app import db

class Product (db.Model):

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String)
    price         = db.Column(db.Float)
    discount      = db.Column(db.Float)
    image_link    = db.Column(db.String)
    image_list    = db.Column(db.String)
    created       = db.Column(db.Integer)
    view          = db.Column(db.Integer)
    buyed         = db.Column(db.Integer)
    warranty      = db.Column(db.String)
    gifts         = db.Column(db.String)
    feature       = db.Column(db.Boolean)

    def __init__(self, name, price, discount, created, view, buyed, warranty, gifts, feature):
        self.name           = name
        self.price          = price
        self.discount       = discount
        self.image_link     = image_link
        self.image_list     = image_list
        self.created        = created
        self.view           = view
        self.buyed          = buyed
        self.warranty       = warranty
        self.gifts          = gifts
        self.feature        = feature

    def __repr__(self):
        return '<Product %r>' %self.id
