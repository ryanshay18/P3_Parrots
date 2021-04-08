from flask import Blueprint, render_template
from flask import request
from minilabs.lola.lolaminilab1 import Math

minilabs_lola = Blueprint("minilabs_lola", __name__,
                          url_prefix="/lola",
                          template_folder="templates",
                          static_folder='static', static_url_path='assets')


@minilabs_lola.route("/minilab", methods=["GET", "POST"])
def lola():
    return render_template("lola/lolaminilab1.html", Math=Math)
