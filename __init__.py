from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Inisialisasi Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwertyuiop890@localhost/aksara_jobs'


# Inisialisasi ekstensi
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'  # Optional: kategori flash message

@login_manager.user_loader
def load_user(user_id):
    from models import User  # ⬅️ Import di sini untuk hindari circular import
    return User.query.get(int(user_id))