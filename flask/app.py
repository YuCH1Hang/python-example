from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import sqlite3
import os
from flask.helpers import flash, url_for

if  "mydb.db" not in os.listdir():
        conn = sqlite3.connect("mydb.db")
        db = conn.cursor()
        db.execute("CREATE TABLE posts (title TEXT, content TEXT, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
        conn.commit()
        conn.close()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name</string:name>
    
#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
    #    return name
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
"'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
"'To understand recursion you must first understand recursion..' -- Unknown",
"'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
"'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
"'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber] </string:name></string:name>

    return render_template(
    'test.html',**locals())

@app.route('/create', methods=["GET", "POST"]) # Allowing Post requests
def create_post():
    if request.method.upper() == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        if title == None or content == None or title.strip() == "" or content.strip() == "":
            # flashes a message to tell the user to fill all the fields
            flash("Please fill all the fields")
            return render_template("create.html")

        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        # Adding the post to the database
        cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)", (title, content))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("display_posts")) # redirect user
    return render_template("create.html")

@app.route("/posts")
def display_posts():
        return render_template("posts.html")
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)