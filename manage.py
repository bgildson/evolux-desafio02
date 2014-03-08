from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db, models

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('run', app.run(debug=True))

if __name__ == '__main__':
	manager.run()