from app import app, db
from flask import render_template, redirect, url_for, request, flash, session, g, Flask
from functools import wraps
from flask_wtf import Form
from forms import RegistrationForm
from flask.ext.sqlalchemy import SQLAlchemy

#import sqlite3



app.secret_key='my previous'
#
#
def login_required(f):
   @wraps(f)
   def wrap(*args,**kwargs):
       if 'logged_in' in session:
           return f(*args, **kwargs)
       else:
           flash('You need to login first')
           return render_template (url_for('index'))
   return wrap
#
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash("You have successfully logged in!")
            return redirect(url_for('signup'))
    return render_template('index.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("you have just logged out")
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == "POST":

        if form.username == "" or form.email== "" or form.password == "" or form.password2 == "" :
            flash("Fill all the fields required")
        else:
            user = signup(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
            confirm = form.password2.data
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
        
    return render_template("signup.html", form=form)


# def connect_db():
#    return sqlite3.connect('posts.db')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
    return render_template("apply.html")

#
#
