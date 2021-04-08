from flask import Blueprint, render_template

from minilabs.michael.michaelminilab1 import startupStack

michael_blueprint = Blueprint("ryan_blueprint", __name__, static_folder="static", template_folder="templates")


@michael_blueprint.route("/minilab")
def michael():
    return render_template("michaelminilab1.html", michaelLab = startupStack())