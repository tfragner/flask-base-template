from app import db, login, ma
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User '{}' with id '{}'>".format(self.username, self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('api.user_detail', id='<id>'),
        'collection': ma.URLFor('api.users')
    })


user_schema = UserSchema()
users_schema = UserSchema(many=True)
