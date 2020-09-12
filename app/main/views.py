from flask import render_template
from app import app
from ..request import get_sources

#views
@app.route('/')
def index():
    
    '''
    view root displaying the index.html template
    '''
    news_sources = get_sources()
    
    return render_template('index.html', news_sources = news_sources)