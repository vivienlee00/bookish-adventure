#Vivien Lee
#SoftDev1 pd7
#HW4 -- Fill Up Yer Flask
#2017-09-20

from flask import Flask

app = Flask("__name__")

@app.route("/")
def hello_world():
    return "hello"

@app.route("/pg2")
def hello_world2():
    return "hello2"

@app.route("/pgCat")
def hello_worldCat():
    return "<img src=\"http://www.petmd.com/sites/default/files/what-does-it-mean-when-cat-wags-tail.jpg\">"

@app.route("/pgBackpack")
def hello_worldBackpack():
    return "<img src=\"https://media.gucci.com/style/DarkGray_Center_0_0_800x800/1478799009/431570_CAO0G_1000_002_086_0000_Light-Soho-leather-chain-backpack.jpg\">"

if __name__ == "__main__":
    app.debug = True
    app.run()

