
from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)

@app.route("/")
def root():
    url = urllib.request.urlopen("https://ghibliapi.herokuapp.com/films?limit=1")
    data = json.loads(url.read())
    title = data[0]['title']

    url = urllib.request.urlopen("https://api.jikan.moe/v3/search/anime?q=CastleintheSky")
    data = json.loads(url.read())
    img = data['image_url']
    
    return render_template("temp.html",
    title=title)

if __name__ == "__main__":
    app.debug = True
    app.run();
