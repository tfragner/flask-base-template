from flask import Blueprint
from flask import redirect, url_for
from flask_login import current_user


bp = Blueprint('blog', __name__)


@bp.before_request
def retrict_bp():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))


from app.blog import routes
