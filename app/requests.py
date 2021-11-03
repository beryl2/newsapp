import urllib.request,json
from .models import News
#news.News = News
api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url,base_url
    api_key = app.config='cae5c5bf402d46888ffa58908123d6e6'
    base_url=app.config= 'https://newsapi.org/v2/everything?q=keyword&apiKey=cae5c5bf402d46888ffa58908123d6e6'

def get_sources():
    source_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=cae5c5bf402d46888ffa58908123d6e6&category=business'
    #_source_url = base_url.format(category, api_key)
    with urllib.request.urlopen(source_url) as url:
        source_data = url.read()
        source_response = json.load(source_data)
        return (source_response)



