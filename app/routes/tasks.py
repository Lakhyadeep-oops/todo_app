from flask import Blueprint, request,redirect,url_for ,Flask,render_template ,flash,session
from werkzeug import Response
from app import db
from app.models import Task

task_bp= Blueprint('tasks',__name__)

@task_bp.route('/')
def view_tasks(): 
    if 'user' not in session:#ie user is not logged in
        return redirect(url_for('auth.login')) # send him to login page 
    task=Task.query.all()

    return render_template('tasks.html',tasks= task)
@task_bp.route('/add',methods=["POST"])
def add_task() -> Response:
    if 'user' not in session:#ie user is not logged in
            return redirect(url_for('auth.login')) # send him to login page 
    title=request.form.get('task')
    if title:
         new_row=Task(title=title,status='Pending')
         db.session.add(new_row)
         db.session.commit()
         flash("TASK ADDED SUCCESSFULLY",'Success')
    return redirect(url_for('tasks.view_tasks'))

@task_bp.route('/toggle/<int:task_id>', methods=['POST'])

def toggle_task(task_id):
     task=Task.query.get(task_id)
     if task:
        if task.status=='Pending':
            task.status='Working'
        elif task.status=='Working':
             task.status='Done'
        
        db.session.commit()

        return redirect(url_for('tasks.view_tasks'))
@task_bp.route('/clear',methods=['POST'])
def clear():
    Task.query.delete()
    db.session.commit()
    flash("ALL TASKS DELETED")
    return redirect(url_for('tasks.view_tasks'))
    
               
