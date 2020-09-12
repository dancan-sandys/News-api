class NewsArticle():
    
    '''
    A class defining  the blueprint of a news article object
    '''
    
    def __init__(self, name,image,description,time):
        
        self.article_name = name
        self.article_image = image
        self.article_description = description
        self.article_time = time
        
        
        
class NewsSource():
    
    '''
    A class defining the blueprint of a news source
    '''
    
    def __init__( self, name, articles, image,)
    
        self.source_name = name
        self.source_articles = articles
        self.source_image = image
        