from . import db


class Properties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(350))
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms=db.Column(db.Integer)
    price = db.Column(db.Float)
    ptype = db.Column(db.String(10))
    location= db.Column(db.String(50))
    photo = db.Column(db.String(250))
    def __init__(self, title, description, num_of_bedrooms, num_of_bathrooms,price,ptype,location,photo):
        self.title = title
        self.description = description
        self.num_of_bedrooms = num_of_bedrooms
        self.num_of_bathrooms = num_of_bathrooms
        self.price=price
        self.ptype=ptype
        self.location=location
        self.photo=photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)
