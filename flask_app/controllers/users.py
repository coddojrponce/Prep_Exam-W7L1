from flask_app import app
from flask import render_template,session,request,redirect

@app.route("/")
def index():
    return render_template("index.html")


# Create
@app.route("/register")
def register():
    pass
# Read
@app.route("/login")
def login():
    pass
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
# Update

# Delete