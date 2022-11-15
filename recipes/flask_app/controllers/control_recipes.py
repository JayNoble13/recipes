from flask_app import app
from flask import render_template, redirect,session,request, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/addnew")
def addnew():
    return render_template("addnew.html")

@app.route("/create" , methods=['post'])
def create():
    data={
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "date_made": request.form["date_made"],
        "time": request.form["time"],
        "user_id": session["user_id"]
    }
    Recipe.create(data)
    return redirect('/home')

@app.route("/edit/<int:id>")
def edit(id):
    data={
        "id":id
    }
    user_data={
        "id":session['user_id']
    }
    return render_template("edit.html", recipe=Recipe.get_one(data), user=User.get_by_id(user_data))

@app.route("/update", methods=['POST'])
def update():
    data={
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "date_made": request.form["date_made"],
        "time": request.form["time"],
        "id": request.form["id"]
    }
    Recipe.update(data)
    return redirect('/home')

@app.route("/deleterecipe/<int:id>")
def destroy(id):
    data={
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/home')

@app.route("/show")
def show():
    return render_template("show.html")