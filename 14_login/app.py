#Imad Belkebir
#SoftDev1 pd7
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
import os
app = Flask(__name__)

user = "Fluffy"
password = "kachow"
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    print(session)
    if 'username' in session.keys():
        return render_template("welcome.html", var1=session['username'])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.form.get('username') != user:
        return render_template("login.html", var1="Error! User does not exist")
    if request.form.get('pass') != password:
        return render_template("login.html", var1="Error! Incorect password")
    session['username'] = request.form.get('username')
    return redirect(url_for("root"))

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run();
