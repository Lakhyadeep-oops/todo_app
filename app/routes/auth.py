from flask import Blueprint, request,redirect,url_for ,Flask,render_template ,flash,session

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='admin' and password=='123':
            session['user']='admin'
            flash("Login Successful",'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid User or Password','danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None )
    flash('Loged Out', 'info')
    return redirect(url_for('auth.login'))
