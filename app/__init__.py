from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from config import Config
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
ma = Marshmallow()
docs = FlaskApiSpec()


def create_app(config_class=Config):
    app2 = Flask(__name__)
    app2.config.from_object(Config)

    db.init_app(app2)
    migrate.init_app(app2, db)
    bootstrap.init_app(app2)
    login.init_app(app2)
    ma.init_app(app2)

    app2.config.update({
        'APISPEC_SPEC': APISpec(
            title='BlaBla',
            version='v1',
            plugins=['apispec.ext.marshmallow'],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })

    docs.init_app(app2)

    from app.api import bp as api_bp
    app2.register_blueprint(api_bp, url_prefix='/api')

    from app.api.users import users, user_detail
    docs.register(users, blueprint='api')
    docs.register(user_detail, blueprint='api')

    from app.main import bp as main_bp
    app2.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app2.register_blueprint(auth_bp)

    from app.blog import bp as blog_bp
    app2.register_blueprint(blog_bp, url_prefix='/blog')

    return app2
