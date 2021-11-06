import os

class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines/sources?apiKey=cae5c5bf402d46888ffa58908123d6e6&category={}'
    NEWS_API_KEY = 'cae5c5bf402d46888ffa58908123d6e6'
 



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    

config_options ={
    'development': DevConfig,
    'production':ProdConfig
}             