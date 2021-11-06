from flask import render_template
from . import main

@main.app_errorhandler(404) #@app.errorhandler
def four_ow_four(error):
    return render_template('fourowfour.html'),404