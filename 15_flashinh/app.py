# Flasking your name -- Imad Belkebir, Theodore Peters
# SoftDev1 pd7
# K15-- Oh yes, perhaps I do...
# 2018-10-02

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
app = Flask(__name__)

user = "Fluffy"
password = "kachow"
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    print(session)
    if 'username' in session and session['username'] == user: # if user already logged in
        return render_template("welcome.html", var1=session['username'])
    return redirect(url_for("login")) # unless logged in default redirects to login screen

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET": # default redirect from route
        return render_template("login.html")
    if request.form.get('username') != user: # if username is invalid
        flash("Error! User does not exist")
        return render_template("login.html")
    if request.form.get('pass') != password: # if password is invalid
        flash("Error! Incorect password")
        return render_template("login.html")
    session['username'] = request.form.get('username') # correct login
    return redirect(url_for("root"))

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run();
