#this file is responsible for checking and testing purpose
#just to see wheather our logging is working or not.


import os 
import sys
from flask import Flask 
from src.logger import logging 
from src.exception import CustomException

"""
This file is just for testing the flask app
Testing exception file
and exception handling 

"""


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():

    try: 
        raise Exception("We are just testing our Exception file")
    except Exception as e: 
        raising_this = CustomException(e, sys)
        logging.info(
            raising_this.error_message
                     )
        
    logging.info("testing purpose")

    return "well, its working" 


#5000
if __name__ == '__main__':
    app.run(debug = True)