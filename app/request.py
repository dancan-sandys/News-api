from app import app
import urllib.request, json
from app.models import NewsSource
from app.models import NewsArticle

#Getting api key

api_key = app.config['NEWS_API_KEY']
sources_base_url = app.config['SOURCES_API_BASE_URL']
articles_base_url = app.config['ARTICLES_API_BASE_URL']



get_sources_url = sources_base_url.format(api_key)


def get_sources():
    '''
    Function that gets a list of the news sources
    '''
    
    with urllib.request.urlopen(get_sources_url) as url:
        
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        
        sources_list = None
        
        if sources_response['sources']:
            sources_retrieved = sources_response['sources']
            sources_list = process_sources(sources_retrieved)
        
        return sources_list

def process_sources(available_sources):
    '''
    Function that processes the list of sources into the NewsSource object blueprint
    '''
    list_of_sources = []
     
    for source in available_sources:
        id = source.get('id')
        name = source.get('name')
        category = source.get('category')
        description = source.get('description')
        
        news_source = NewsSource(id,name,category,description)
        list_of_sources.append(news_source)
    
    return list_of_sources
        
    
def get_articles(source_id):
    '''
    function retirieving required articles
    '''
    
    
    get_artcles_url = articles_base_url.format(source_id, api_key)
   
    with urllib.request.urlopen(get_artcles_url) as url:
        news_articles_data = url.read()
        news_articles_responses = json.loads(news_articles_data)
       
        articles_list = None
       
        if news_articles_responses['articles']:
           news_articles = news_articles_responses['articles']
           articles_list = process_articles(news_articles)
           
           
        return articles_list
    
    
def process_articles(articles_to_be_processed):
    '''
    function processing the articles into the NewsArticles objects
    '''
    
    list_of_articles = []
    
    for new_article in articles_to_be_processed:
        name = new_article.get('title')
        image = new_article.get('urlToImage')
        description = new_article.get('description')
        time = new_article.get('publishedAt')
        url_to_site = new_article.get('url')
    
    
        new_article = NewsArticle(name,image,description,time,url_to_site)
        list_of_articles.append(new_article)
    
    return list_of_articles
    


