#2nd file to operate on 
#here we make the table and stuff 

from app import db

class Task(db.Model):
    id =db.Column(db.Integer , primary_key=True)
    title=db.Column(db.String(100) ,nullable=False)
    status=db.Column(db.String(20))
