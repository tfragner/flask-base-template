from flask import render_template
from app.auth import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', title='Sign In')
