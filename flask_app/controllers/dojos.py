from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route("/add/dojo", methods = ["POST"])
def add_dojo():
    Dojo.save(request.form)
    return redirect("/dojos")

@app.route("/dojo/<int:id>")
def view(id):
    data = {
        "id": id
    }
    return render_template("dojo.html", dojo = Dojo.get_one_join_ninja(data))
