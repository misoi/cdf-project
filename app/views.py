from app import app
from flask import render_template, redirect, url_for, request, flash, session, g, Flask
from functools import wraps
from flask_wtf import Form
from forms import RegistrationForm
##from flask.ext.sqlalchemy import SQLAlchemy
import sqlite3
#
#
#
##def login_required(f):
##    @wraps(f)
##    def wrap(*aegs,**kwargs):
##        if 'logged_in' in session:
##            return f(*args, **kwargs)
##        else:
##            flash('You need to login first')
##    return wrap
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
def logout():
    session.pop('logged_in', None)
    flash("you have just logged out")
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm = form.password2.data
    return render_template("signup.html", form=form)

##@app.route('/index')
##def db():
##    flash("Sucessfully registered")
##    return render_template("index.html")
#
@app.route('/about')
def about():
    return render_template("about.html")
#
#
