
from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)

@app.route("/")
def root():
    url = urllib.request.urlopen("https://www.boredapi.com/api/activity")
    data = json.loads(url.read())
    return render_template("temp.html",
    activity=data['activity'],
    acc=data['accessibility'],
    type=data['type'],
    par=data['participants'],
    pri=data['price'])

if __name__ == "__main__":
    app.debug = True
    app.run();
