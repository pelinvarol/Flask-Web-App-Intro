from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # db'yi app ile ilişkilendiriyoruz


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # /auth/ olabilir mesela, o zaman /auth/ yazdıktan sonra login, signup, logout gibi şeyler yazılabilir

    from .models import User, Note # import the User and Note models

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # login olunmadıysa yönlendirmesi gereken yer yani login sayfası
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_load(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    return app

#this is going to check if database is already exists, and if not, it will create a new one
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')