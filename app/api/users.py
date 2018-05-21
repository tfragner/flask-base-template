from flask import jsonify
from app.models.user import User, users_schema, user_schema
from app.api import bp


@bp.route('/users', methods=['GET'])
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


@bp.route('/users/<id>', methods=['GET'])
def user_detail(id):
    user = User.query.get_or_404(int(id))
    return user_schema.jsonify(user)
