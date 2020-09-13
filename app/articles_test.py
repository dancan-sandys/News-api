import unittest
from models import NewsArticle

class TestArticles(unittest.TestCase):
    
    def setUp(self):
        
        self.new_articles = NewsArticle('Dancan','leon','Sandys','27/12/1999', 'Yesterday')
        
    def test_initialize(self):
        self.new_articles
        self.assertTrue(isinstance(self.new_articles, NewsArticle))    
        
if __name__ == '__main__':
    unittest.main()