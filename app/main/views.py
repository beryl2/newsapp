from flask import render_template,request,redirect, url_for
from . import main
from ..requests import get_sources 
#from . forms import ReviewForm
from ..models import Review


@main.route('/')
def index():

    



    return render_template('index.html')