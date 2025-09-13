from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Inisialisasi eksternal
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['UPLOAD_FOLDER'] = 'uploads'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import blueprint di sini supaya tidak circular import
    from routes.user_routes import user_bp
    from routes.admin_routes import admin_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
