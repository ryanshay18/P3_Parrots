from flask import Blueprint, render_template

from minilabs.michael.michaelminilab1 import Pigeon

minilabs_michael = Blueprint('minilabs_michael', __name__,
                              url_prefix="/michael",
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@minilabs_michael.route("/minilab")
def michael():
    return render_template("michael/michaelminilab1.html", pigeon=Pigeon(20))