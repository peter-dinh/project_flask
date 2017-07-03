from app import db

class News(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    intro = db.Column(db.String)
    content = db.Column(db.String)
    image_link = db.Column(db.String)
    meta_desc = db.Column(db.String)
    meta_key = db.Column(db.String)
    created = db.Column(db.Integer)
    count_view = db.Column(db.Integer)
    feature = db.Column(db.Boolean)

    def __init__(self, title, intro, content, image_link, meta_desc, meta_key, created, count_view, feature):
        self.title = title
        self.intro = intro
        self.content = content
        self.image_link = image_link
        self.meta_desc = meta_desc
        self.meta_key = meta_key
        self.created = created
        self.count_view = count_view
        self.feature = feature

