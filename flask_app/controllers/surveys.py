from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.cls import Surv

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/viewinfo", methods=["POST"])
def validate():
    if Surv.validate(request.form):
        Surv.save_info(request.form)
        return redirect("/view")
    else:
        return redirect("/")

@app.route("/view")
def view():
    x = Surv.get_info()
    return render_template("view.html", info=x)

