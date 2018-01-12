import os
from app import create_app
#from app import db
#from app.models import User, Role


app = create_app("")
if __name__ == "__main__":
    run_conf = dict(
        debug=True,
        host="0.0.0.0",
        port=2000,
    )
    app.run(**run_conf)
