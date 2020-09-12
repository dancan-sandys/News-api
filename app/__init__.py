from flask import Flask
from config import DevConfig

#initializing the application

app = Flask(__name__)



#setting up the configurations
app.config.from_object(DevConfig)
from .main import views