from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap



#initializing the application

app = Flask(__name__,instance_relative_config=True)



#setting up the configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initializing flask extensions
bootstrap = Bootstrap(app)


from .main import views