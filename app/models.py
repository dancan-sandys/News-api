class NewsArticle():
    
    '''
    A class defining  the blueprint of a news article object
    '''
    
    def __init__(self, name,image,description,time, url_to_site):
        
        self.article_name = name
        self.article_image = image
        self.article_description = description
        self.article_time = time
        self.url_to_site =url_to_site
        
        
        
class NewsSource():
    
    '''
    A class defining the blueprint of a news source
    '''
    
    def __init__( self,id, name, category, description):
    
        self.source_id = id
        self.source_name = name
        self.source_category = category
        self.source_description = description
        