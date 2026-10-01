from flask import Flask #this is the first file i will work on 
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() # initialise the database 

def create_app():
    app=Flask(__name__) #initialise app
    app.config['SECRET_KEY']='mysecretkey' #this
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///task.db' #database location
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    from app.routes.auth import auth_bp  # import the modules 
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp) # use the blueprints of the modules 
    app.register_blueprint(task_bp)

    return app