from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String


def inciar():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)

    return app, db


app, db = inciar()


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    todos = db.relationship("Todo", back_populates="usuario")

    def __repr__(self):  # optional
        return f'Forma {self.name}'


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String)
    fecha = db.Column(db.String)
    is_done = db.Column(db.Boolean, unique=False, default=True)
    parent = db.relationship("Usuario", back_populates="todos")
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

    def __repr__(self):  # optional
        return f'todos {self.name}'


db.create_all()

print(1)
