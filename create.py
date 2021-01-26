from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    country = db.Column(db.String(255), unique=False, nullable=False)


if __name__ == "__main__":
    """create each table"""
    db.create_all()

    try:
        u1 = Users(name='William', country='USA')
        u2 = Users(name='Valerie', country='Russia')
        u3 = Users(name='Lola', country='Russia')
        u4 = Users(name='Michael', country='White')
        u5 = Users(name='Beakers', country='Torts')
        u6 = Users(name='John Mortensen', country='DNHS')

        session.add_all([u1, u2, u3, u4, u5, u6])
        session.commit()

    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print(row.country)
