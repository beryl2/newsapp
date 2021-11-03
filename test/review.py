import unittest
from app.models import News
class Movietest(umitest,testCase):
    def setup(self):
        self.new_news = News

    def test_instance(self):
        self.assertTRUE(isinstance(self.new_news,News))    
