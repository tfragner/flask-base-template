from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app, db
from app.models.user import User


app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

    
if __name__ == '__main__':
    manager.run()
