from flask import render_template, redirect, url_for
from . import main
from ..request import get_sources
from ..request import get_articles


#views
@main.route('/' )
def index():
    
    '''
    view root displaying the index.html template
    '''
    news_sources = get_sources()
    
    return render_template('index.html', news_sources = news_sources)

@main.route('/articles/<source_id>')
def articles(source_id):

    '''
    articles root that display the articles.html template
    '''
    
    news_articles = get_articles(source_id)
    
    
    
    return render_template('articles.html', articles = news_articles)
