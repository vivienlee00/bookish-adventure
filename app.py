#Vivien Lee
#SoftDev1 pd7
#HW4 -- Fill Up Yer Flask
#2017-09-20

from flask import Flask, render_template
import urllib2
import json

app = Flask("__name__")



@app.route("/")
def hello_world():
    siteurl = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=TUVnwOk0lvflM6FqvNJRUzyuVcHTN1ciFHPip9dU")
    siteurl2= siteurl.read()
    elements = json.loads(siteurl2)
    return render_template('temp.html', img = elements["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()

