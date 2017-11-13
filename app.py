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
    return render_template('temp.html', img = elements["url"], exp = elements["explanation"])

@app.route("/flickr")
def test_flickr():
    siteurl = urllib2.urlopen("https://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key=0163f6e2944d794716ea1001a8149b7d&photo_id=22235517575&format=json")
    siteurl2= siteurl.read()
    siteurl3= siteurl2[14:-1]
    elements = json.loads(siteurl3)
    farmid = str(elements['photo']['farm'])
    serverid = str(elements['photo']['server'])
    photoid = str(elements['photo']['id'])
    secretid = str(elements['photo']['secret'])
    formid = str(elements['photo']['originalformat'])
    imgurl = 'https://farm' + farmid + '.staticflickr.com/' + serverid + '/'+ photoid + '_' + secretid + '.' + formid
    author = 'Photo by ' + elements['photo']['owner']['realname']
    return render_template('temp.html', img = imgurl, exp = author)

if __name__ == "__main__":
    app.debug = True
    app.run()
