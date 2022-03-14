from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import dojo, ninja



@app.route("/ninjas")
def ninjas():
    return render_template("ninja.html", dojos= dojo.Dojo.get_all())

@app.route("/process", methods=["POST"])
def submit():
    ninja.Ninja.save(request.form)
    return redirect("/")
