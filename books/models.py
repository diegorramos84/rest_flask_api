from .. import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(500), nullable=False)
    stars = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, stars={self.stars}"
