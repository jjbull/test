from flask import Flask

app= Flask(__name__)

app.secret_key ='developments key'

app.config ['SQLALCHEMY_DATABASE_URI'] ='mysql://root@localhost/development'

from models import db
db.init_app(app)

import intro_to_flask.routes