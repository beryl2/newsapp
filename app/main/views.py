from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_newses,get_news,search_news
from . forms import ReviewForm
from ..models import review
Review = review.Review

@main.route('/')
def index():

    business_news = get_news('business')
    print(business_news)
    sports_news = get_news('sports')
    print(sports_news)
    entertainment_news = get_news('entertainment')
    print(entertainment_news)
    health_news = get_news('health')
    print(health_news)

    message = 'hello world'
    title = 'news updates'
    
    #search_movie = request.args.get('movie_query')
    #if search_news:
        #return redirect(url_for('search',news_name= search_news))
#else
@main.route('/news/<int:id>')
def news(id):
    news = get_news(id)
    title = f'{news.title}'


@main.route('/search/<news_name>')
def search(news_name):
    news_name_list = news_name.split(" ") 
    news_name_format = '+'.join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'

@main.route('/news/review/new/<int:id>', methods =['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)
    if form. validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id, title, news.poster, review)
        new_review.save_review()
        return redirect(url_for('news', id = news.id))

    title = f'{news.title} review'    
    return render_template('index.html','news.html' message = message, title=title, business=business_news, sports = sports_news, entertainment = entertainment_news, health = health_news, 'search.html' news=searched_news, 'new_review.html', title = title,review_form = form, news= news )