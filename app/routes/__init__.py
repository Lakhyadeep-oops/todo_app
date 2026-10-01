from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() #creates database 

def create_app():
    app=Flask(__name__)
    
