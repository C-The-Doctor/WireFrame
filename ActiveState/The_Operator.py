from flask import g
from flask import Flask  , url_for , render_template , request , redirect 
from flask.views import View
from flask import g 
import os , random , string 
from werkzeug.utils  import secure_filename
import time
import sqlite3
from sqlite3 import Error
import uuid 
import datetime




app=Flask(__name__)





# CLASS BASED VIEW DECLARATIONS 
# Clothes & General Accessories 




# CLASS BASED VIEW DECLARATIONS 
# Clothes & General Accessories 



# Function To Return Sequence Strings For Token Synchronixation 


def Generate_Sequence():
    return uuid.uuid4()  





class BackLog(View):
    def dispatch_request(self):
        UserID = ""
        return render_template('BackLog.html', UserID = UserID )























app.add_url_rule('/', view_func=BackLog.as_view('Home'))






if __name__=='__main__':
   app.run(host="0.0.0.0" , debug="False" )
