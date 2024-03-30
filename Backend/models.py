from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True) # In python Snake Case is convention (using underscore)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self): # To take all objects from above and convert them into a python dictionary, which we can then convert into JSON, which can be passed from our API
        return {
            "id": self.id, # In JSON files it's a convention to use Camel Case fields
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }