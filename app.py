from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_required, login_user
from datetime import datetime
import pytz

app = Flask(__name__)
app.secret_key = 'mysecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(request.form['username'])
        login_user(user)
        return redirect(url_for('time'))
    return render_template('login.html')

@app.route('/time')
@login_required
def time():
    now = datetime.now(pytz.timezone('US/Central'))
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('time.html', time=formatted_time)

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1')
