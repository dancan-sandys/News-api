class Config:
    
    '''
    General configurations parent class
    '''
    
    pass

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