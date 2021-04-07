from flask import Blueprint, render_template
from flask import request
from minilabs.lola.lolaminilab1 import Math

lola_blueprint = Blueprint("lola_blueprint", __name__, static_folder="static", template_folder="templates")


@lola_blueprint.route("/lolaminilab", methods=["GET", "POST"])
def lola():
    return render_template("lolaminilab1.html", Math=Math)