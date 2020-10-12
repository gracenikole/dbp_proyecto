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

    id = db.Column(Integer, primary_key=True)
    user_name = db.Column(String)
    email = db.Column(String)
    password = db.Column(String)
    todos = relationship("Todo", back_populates="usuario")

    def __repr__(self):  # optional
        return f'Forma {self.name}'


class Todo(db.Model):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    descripcion = db.Column(String)
    fecha = db.Column(Date)
    is_done = db.Column(bool)
    parent = relationship("Usuario", back_populates="todos")

    def __repr__(self):  # optional
        return f'todos {self.name}'


db.create_all()

print(1)
