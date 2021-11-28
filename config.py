import os

class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}&category={}'
    NEWS_BASE_URL_HEADLINES = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = 'cae5c5bf402d46888ffa58908123d6e6'
 



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    

config_options ={
    'development': DevConfig,
    'production':ProdConfig
}             