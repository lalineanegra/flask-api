import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init app
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__)) #getting the directory of the current file

# Configuring a basic Sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "my_db.sqlite")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db Sqlite
db = SQLAlchemy(app)

# Initialize Marshmallow, object serialization/de-serialization library)
ma = Marshmallow(app)

# Using SQLALchemy ORM; create a model to interact with the database:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    occupation = db.Column(db.String(200))
    income = db.Column(db.Float)
    password = db.Column(db.String(200)) #TODO: password must be hashed before saving!

    def __init__(self, name, occupation, income, password):
        self.name = name
        self.occupation = occupation
        self.income = income
        password = password

#Define a schema with Marshmallow 
class UserSchema(ma.Schema):
    class Meta: #define the fields that are allowed to be shown
        fields = ('id', 'name', 'occupation', 'income')

user_schema = UserSchema()
users_Schema = UserSchema(many=True)

# Defining routes and methods for the API
@app.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    occupation = request.json['occupation']
    income = request.json['income']
    password = request.json['password']

    #Save new user
    new_user = User(name, occupation, income, password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# RunServer
if __name__ == '__main__':
    app.run(debug=True)