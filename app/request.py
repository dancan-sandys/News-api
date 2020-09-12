from app import app
import urllib.request, json
from app.models import NewsSource


#Getting api key

api_key = app.config['NEWS_API_KEY']
sources_base_url = app.config['SOURCES_API_BASE_URL']
articles_base_url = app.config['ARTICLES_API_BASE_URL']

source = 'Bitcoin'

get_sources_url = sources_base_url.format(api_key)
get_artcles_url = articles_base_url.format(source, api_key)

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
        name = source.get('name')
        category = source.get('category')
        description = source.get('description')
        
        news_source = NewsSource(name,category,description)
        list_of_sources.append(news_source)
    
    return list_of_sources
        
    
    
   
    
    
    


