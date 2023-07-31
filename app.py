from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_required, login_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jenkins:jenkins@<your-ec2-db-host>/jenkins'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin): 
    id = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            user = User.query.get(username)
            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user.password, request.form['password']):
                error = 'Incorrect password.'
            else:
                login_user(user)
                return redirect(url_for('time'))
        except Exception as e:
            error = 'Error logging in: {}'.format(e)
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = generate_password_hash(request.form['password'])

            # check if username already exists
            if User.query.get(username) is not None:
                error = 'User {} is already registered.'.format(username)
            else:
                # store the new user
                new_user = User(id=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                return "User {} created successfully".format(username)
        except Exception as e:
            error = 'Error signing up: {}'.format(e)
    return render_template('signup.html', error=error)

@app.route('/time')
@login_required
def time():
    now = datetime.now(pytz.timezone('US/Central'))
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('time.html', time=formatted_time)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
