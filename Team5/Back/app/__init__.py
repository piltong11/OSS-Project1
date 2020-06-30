from flask import Flask

app = Flask(__name__)

from app.index import cover as cover
from app.index import option as option
from app.index import weather as weather
from app.index import fashion as fashion

app.register_blueprint(cover)
app.register_blueprint(option)
app.register_blueprint(weather)
app.register_blueprint(fashion)
