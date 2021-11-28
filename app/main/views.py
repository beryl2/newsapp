from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news,get_headlines
from . forms import ReviewForm


@main.route('/')
def index():

    business_news = get_news('business')
    
    sports_news = get_news('sports')

    entertainment_news = get_news('entertainment')
    
    health_news = get_news('health')
    

    message = 'hello world'
    title = 'news updates'

    return render_template('index.html', message = message, title = title, business = business_news, sports = sports_news, entertainment = entertainment_news, health = health_news )
    
    
@main.route('/news/<int:id>')
def news(id):
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title, news = news)

@main.route("/headlines/<id>")
def articles(id):
  articles = get_headlines(id)
   


  return render_template('headlines.html', articles = articles  )



    

