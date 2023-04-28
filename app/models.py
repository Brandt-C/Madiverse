from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RawStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rstring = db.Column(db.String, nullable=False)

    def __init__(self, rstring):
        self.rstring = rstring
    
    def saveStory(self):
        db.session.add(self)
        db.session.commit()