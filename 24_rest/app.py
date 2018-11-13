
from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def root():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=5IRdvy3xah6vato5f9aGiOlqv5WXDpP2khv2nItV")
    data = json.loads(url.read())
    return render_template("temp.html", data["url"])

if __name__ == "__main__":
    app.debug = True
    app.run();
