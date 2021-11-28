import urllib.request,json
from .models import News, Headlines

api_key = None #app.config['NEWS_API_KEY']
base_url = None # app.config['BASE_URL']
base_url_headlines = None

def configure_request(app):
    global api_key,base_url,base_url,base_url_headlines
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL'] 
    base_url_headlines = app.config['NEWS_BASE_URL_HEADLINES']

def get_news(category):
    get_news_url= base_url.format(api_key, category)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']: 
            news_source_list = get_news_response['sources']
            news_sources = process_results(news_source_list)
   
    return news_sources  


def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')

        single_source = News(id,name,description,category)
        news_results.append(single_source)
           
    return news_results

def get_headlines(id):
    get_news_url= base_url_headlines.format(id, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['articles']: 
            news_source_list = get_news_response['articles']
            news_sources = process_headlines(news_source_list)
   
        return news_sources 

def process_headlines(article_list):
    news_results = []
    for article_item in article_list:
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')

        single_article = Headlines(title,urlToImage,url,description,publishedAt)
        news_results.append(single_article)
           
    return news_results










               












