from app import db

class Comment(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    product_id  = db.Column(db.Integer)
    parent_id   = db.Column(db.Integer)
    user_name   = db.Column(db.String)
    user_mail   = db.Column(db.String)
    user_id     = db.Column(db.Integer)
    user_ip     = db.Column(db.String)
    content     = db.Column(db.String)
    created     = db.Column(db.Integer)
    count_like  = db.Column(db.Integer)
    status      = db.Column(db.Integer)

    def __init__(self, product_id, parent_id, user_name, user_mail, user_id, user_ip, content, created):
        self.parent_id      = product_id
        self.parent_id      = parent_id
        self.user_name      = user_name
        self.user_mail      = user_mail
        self.user_id        = user_id
        self.user_ip        = user_ip
        self.content        = content
        self.created        = created
        self.count_like     = 0
        self.status         = 0


    def add_cmt_in_clinet(self, product_id, parent_id, user_name, user_mail, user_id, user_ip, content, created):

        self.parent_id = product_id
        self.parent_id = parent_id
        self.user_name = user_name
        self.user_mail = user_mail
        self.user_id = user_id
        self.user_ip = user_ip
        self.content = content
        self.created = created
        self.count_like = 0
        self.status = 0

    def change_status(self):
        self.status = 1

    def like(self):
        self.count_like = self.count_like + 1

    def dislike(self):
        self.count_like = self.count_like - 1


