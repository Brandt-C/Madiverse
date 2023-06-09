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

class Character(db.Model):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String)
    full_name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    img = db.Column(db.String)
    uni = db.Column(db.String)

    def __init__(self, id, full_name, desc, img, first_name, uni):
        self.id = id,
        self.full_name = full_name,
        self.desc = desc,
        self.img = img,
        self.first_name = first_name, 
        self.uni = uni
    
    def saveChar(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'first_name' : self.first_name,
            'full_name' : self.full_name,
            'desc' : self.desc,
            'img' : self.img,
            'uni' : self.uni
        }
    
class Location(db.Model):
    id = db.Column(db.String, primary_key=True)
    uni = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    residents = db.Column(db.String, nullable=False)

    def __init__(self, id, uni, name, desc, residents):
        self.id = id,
        self.uni = uni,
        self.name = name,
        self.desc = desc,
        self.residents = residents
    
    def saveLoc(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id' : self.id,
            'uni' : self.uni,
            'name' : self.name,
            'desc' : self.desc,
            'residents' : self.residents
        }
    