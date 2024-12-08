from flask import (
    render_template, 
    url_for, 
    flash, 
    redirect,
    request
)
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import (
    login_user, 
    current_user, 
    logout_user, 
    login_required
)


posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 16, 2024'
    },
    {
        'author': 'Esther Brown',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 17, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # create a new instance of the user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # add user to the changes that is to be made to the database
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created! You are now able to login', 'success')
        print(f'Your Account has been created! You are now able to login')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # checks if the email enter by the user matcher what we have in the db, if so the system should match the first user with that email within the db 
        user = User.query.filter_by(email=form.email.data).first()
        # checks if user exist and the password they enter matches what we have n the db then, they must be login.
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title="Account")

    