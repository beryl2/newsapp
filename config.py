import os

class Config:
    NEWS_BASED_URL='https://newsapi.org/v2/top-headlines/sources?apiKey=cae5c5bf402d46888ffa58908123d6e6&category=business'

 



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    

config_options ={
    'development': DevConfig,
    'production':ProdConfig
}             