from flask import Flask, request, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

form = """ 

"""
@app.route("/")
def index():
    return render_template('homepage.html')

app.run()