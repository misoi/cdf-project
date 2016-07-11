from app import app
from flask import render_template, redirect, url_for, request, flash, session, g, Flask

from flask_bcrypt import check_password_hash
from flask_login import LoginManager, logout_user, login_required, current_user, login_user
import models
from forms import LoginForm, RegisterForm,DetailForm,PlacedetailForm,SchooldetailForm

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid )
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response


#======================index route=============


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
  return render_template('index.html')


#======================login route=============


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("you email or password doesn't match", "error")

        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("logged in as")
                return redirect(url_for('apply'))
            else:
                flash("you email or password doesn't match", "error")
    return render_template('login.html', form=form)


#======================logout route=============
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    logout_user()
    flash("you have just logged out")
    return redirect(url_for('index'))


#======================registration  route=============
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('you registered', "success")
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


#======================about  route=============
@app.route('/about')
def about():
    return render_template("about.html")


#======================personal details route=============
@app.route('/detail', methods=['GET', 'POST'])
@login_required
def apply():
    form = DetailForm()
    if form.validate_on_submit():
        models.Personal.create_user(
            fname=form.fname.data,
            sname=form.sname.data,
            email=form.email.data,
            nid=form.nid.data
        )
        flash("you application has been send successfuly")
        return redirect(url_for('place'))
    return render_template("apply.html", form=form)

#======================place deatils route=============
@app.route('/place', methods=['GET', 'POST'])
@login_required
def place():
    form = PlacedetailForm()
    if form.validate_on_submit():
        models.Place.create_user(
            county=form.county.data,
            constituency=form.constituency.data,
            ward=form.ward.data,
            location=form.location.data,
            slocation=form.slocation.data,
            village=form.village.data
        )
        flash("your details has been saved successfuly")
        return redirect(url_for('school'))
    return render_template("place.html", form=form)

#======================school details route=============
@app.route('/school', methods=['GET', 'POST'])
@login_required
def school():
    form = SchooldetailForm()
    if form.validate_on_submit():
        models.School.create_user(
            college=form.college.data,
            year=form.year.data
        )
        flash("you application has been send successfuly")
        return redirect(url_for('upload'))
    return render_template("school.html", form=form)

#======================school details route=============
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():

    return render_template("upload.html")
