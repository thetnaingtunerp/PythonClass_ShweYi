from flask import Flask
from flask import render_template, Response
import sqlite3


app = Flask(__name__)

@app.route("/")
def hello_world():
    con = sqlite3.connect('firstdb.db')
    con.cursor()   #db open
    
    return render_template('index.html') #user view


app.run()