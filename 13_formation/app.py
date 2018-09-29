#Imad Belkebir
#SoftDev1 pd7
#K12 --
#2018-09/27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("temp.html")

@app.route("/auth", methods=['GET','POST'])
def form():
    if(request.method == 'GET'):
        return 'The username entered was <font color="red">' + \
          request.args['username'] + '</font><br>The request method used was <font color="blue">' + \
          request.method + '</font><br><font color="purple">Thanks'
    else:
        return 'The username entered was <font color="red">' + \
          request.form['username'] + '</font><br>The request method used was <font color="blue">' + \
          request.method + '</font><br><font color="purple">Thanks'
if __name__ == "__main__":
    app.debug = True
    app.run();
