from main import app, db
from flask_migrate import Migrate


migrate = Migrate(app, db)


