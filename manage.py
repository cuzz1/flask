import os
from app import create_app
from flask_script import Manager, Shell
from app import db
#from app.models import User, Role


app = create_app(os.getenv("FLASK_CONFIG") or "default")
manage = Manager(app)
shell = Shell(app)

if __name__ == "__main__":
    run_conf = dict(
        debug=True,
        host="0.0.0.0",
        port=2000,
    )
    db.create_all()
    app.run(**run_conf)
    #manage.run()
