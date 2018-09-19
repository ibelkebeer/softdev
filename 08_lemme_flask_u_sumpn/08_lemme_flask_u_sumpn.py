#Imad Belkebir
#SoftDev1 pd7
#K8 -- Lemme flask u sumn
#2018-09-18

from flask import Flask
app = Flask(__name__)

@app.route('/')
def page1():
    return '<a href=/page2>page 2</a> <br> <a href=/page3>page 3</a>'

@app.route('/page2')
def page2():
    return '<a href=/>page 1</a> <br> <a href=/page3>page 3</a>'

@app.route('/page3')
def page3():
    return '<a href=/>page 1</a> <br> <a href=/page2>page 2</a>'

app.debug = True
app.run()
