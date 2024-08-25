import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology,login_required
from datetime import datetime

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///templates/reads.db")
data = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
@login_required
def home():
    posts = db.execute("SELECT * FROM posts")
    return render_template('index.html',posts=posts)


# Login

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = data.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


# Logout
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



#register
@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    # ensure the user reaches via post i.e. has submitted form in register.html
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Must Give Username")

        if not password:
            return apology("Must Give Password")
        # ensure password confirmation was submitted
        if not confirmation:
            return apology("Must Give Confirmation")
        # ensure password and confirmation match
        if password != confirmation:
            return apology("Password Do Not Match")

        # create a hashed version of a password
        hash = generate_password_hash(password)

        try:
            new_user = data.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
            )
        except:
            # username already exists,so insertion would fail and will return apology api meme
            return apology("Username already exists")

        # stores the new user's ID in the session.
        session["user_id"] = new_user

        return redirect("/")







#contact i.e data from webpage to database
@app.route("/contact")
def contact():
    return render_template('contact.html')

# sql contacts is being linked to database
@app.route("/contact", methods=["POST"])
def Contact():
    if request.method == "POST":
        email = request.form['email']
        aboutself = request.form['aboutself']
        concern = request.form['concern']

        db.execute("INSERT INTO contacts (email,aboutself,concern) VALUES(?, ?,?)",
                   email, aboutself, concern)
        return "Your query has been received."

    else:
        return render_template("contact.html")

@app.route("/add")
def add():
    return render_template('add.html')

# sql contacts is being linked to database
@app.route("/add", methods=["POST"])
def Add():
    if request.method == "POST":
        slug = request.form['slug']
        title = request.form['title']
        content = request.form['content']

        db.execute("INSERT INTO posts (slug,title,content) VALUES(?, ?,?)",
                   slug, title, content)
        return "Your post has been submitted."

    else:
        return render_template("add.html")



# sql posts is being linked to database and create route

@app.route("/post/<string:post_slug>", methods=["GET"])
def Post(post_slug):

        post = db.execute("SELECT * FROM posts WHERE slug = ?", (post_slug,))[0]

        return render_template("post.html",post=post)



@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog1")
def blog1():
    return render_template('blog1.html')


@app.route("/helper_c")
def helper_c():
    return render_template('helper_c.html')


@app.route("/filter_c")
def filter_c():
    return render_template('filter_c.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route("/tideman")
def tideman():
    return render_template('tideman.html')
