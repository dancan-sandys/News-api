from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourOfour(error):
    '''
    function to render the 404 page when there is a 404 error
    '''
    
    return render_template('fourOfour.html'),404
    