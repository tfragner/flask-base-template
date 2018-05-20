from flask import render_template
from app.blog import bp


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('blog/index.html', title='Blog')
