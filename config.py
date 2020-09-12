class Config:
    
    '''
    General configurations parent class
    '''
    
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
        
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'

class DevConfig(Config):
    '''
    Development configuration child class
    
    
    Args:
        Config: Parent class with general configurations
    '''
    
    DEBUG = True
    
class ProdConfig(Config):
    
    '''
    Production configuration child class
    
    Args:
        Config: parent class with general configuration settings
    '''
    
    pass