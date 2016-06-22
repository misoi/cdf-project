from app import app, db
from flask import render_template, redirect, url_for, request, flash, session, g, Flask
from functools import wraps
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy

#import sqlite3


def login_required(f):
   @wraps(f)
   def wrap(*args,**kwargs):
       if 'logged_in' in session:
           return f(*args, **kwargs)
       else:
          flash('You need to login first')
          return render_template ("index.html")
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
            return redirect(url_for('apply'))
    return render_template('index.html', error=error)

@app.route('/logout')

def logout():
    session.pop('logged_in', None)
    flash("you have just logged out")
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == "POST":
      user = signup(request.form['username'],
      request.form['email'], 
      request.form['password'],
      request.form['confirm']    
      )
      db.session.add(user)
      db.session.commit()
      flash("You;ve successd")
        
    return render_template("signup.html")



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
  if request.method == "POST":
      apply = Apply(request.form['fname'],   
      request.form['sname'], 
      request.form['email'],
      request.form['nid'], 
      request.form['ward'], 
      request.form['location'],
      request.form['slocation'],
      request.form['village'], 
      request.form['college'],
      request.form['year']    
      )
      db.session.add(apply)
      db.session.commit()
      flash("your application has been successfuly submited")
  return render_template("apply.html")
