from flask import render_template
from app import app

#views
@app.route('/')
def index():
    
    '''
    view root displaying the index.html template
    '''
    
    return render_template('index.html')