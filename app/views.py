from app import app
from flask import render_template, redirect, url_for, request
from flask import Flask

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password'
        else:
            return redirect(url_for(''))
#    return "Hello, World!"
    return render_template("index.html", error=error)

