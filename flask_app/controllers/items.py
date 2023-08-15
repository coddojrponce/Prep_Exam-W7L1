from flask_app import app     
from flask import render_template,redirect,request
from flask_app.models.item import Item

@app.route("/items")
def dash():
    return render_template("dash.html",items=Item.get_all())

@app.route("/items/new")
def create_item():
    return render_template("create.html")

@app.route("/items/<int:id>/edit")
def edit_item(id):
    item=Item.get_one(id)
    return render_template("edit.html",item=item)

@app.route("/items/<int:id>/view")
def view_one_item(id):
    item=Item.get_one(id)
    return render_template("view_one.html",item=item)

# Create

@app.route("/items/create",methods=['POST'])
def create():
    Item.save(request.form)
    return redirect("/items")

# Read 

# Update
@app.route("/items/update",methods=['POST'])
def update():
    
    Item.update(request.form)
    return redirect("/items")

# Delete

@app.route('/items/delete/<int:id>')
def delete(id):
    Item.delete(id)
    return redirect('/items')