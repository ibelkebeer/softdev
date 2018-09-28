#
#
#
#

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def root():
    

if __name__ == "__main__":
    app.debug = True
    app.run();
