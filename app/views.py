from app import app
from flask import render_template, redirect, url_for, request, flash, session
from flask import Flask
from functools import wraps

@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash("You have successfully logged in!")
            return redirect(url_for('logout'))
#    return "Hello, World!"
    return render_template("index.html", error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("you have just logged out")
    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    return render_template("signup.html")

