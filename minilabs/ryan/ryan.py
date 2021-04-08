from flask import Blueprint, render_template

from minilabs.ryan.ryanminilab1 import startupStack

ryan_blueprint = Blueprint("ryan_blueprint", __name__, static_folder="static", template_folder="templates")


@ryan_blueprint.route("/minilab")
def ryan():
    return render_template("ryanminilab1.html", ryanLab = startupStack())
