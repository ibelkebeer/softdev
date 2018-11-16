
from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)

@app.route("/")
def root():
    url = urllib.request.urlopen("https://ghibliapi.herokuapp.com/films?limit=1")
    data = json.loads(url.read())

    #print(data)

    title = data[0]['title']

    url = urllib.request.urlopen("https://api.jikan.moe/v3/search/anime?q=Kob")
    data = json.loads(url.read())

    #print(data)

    img = data['results'][1]['image_url']

    url = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    data = json.loads(url.read())

    #print(data)

    return render_template("temp.html",
    title=title,
    pic1=img,
    pic2=data['message'])

if __name__ == "__main__":
    app.debug = True
    app.run();
