from flask import Blueprint, render_template

from minilabs.ryan.ryanminilab1 import startupStack

minilabs_ryan = Blueprint("minilabs_ryan", __name__,
                          url_prefix="/ryan",
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@minilabs_ryan.route("/minilab")
def ryan():
    return render_template("ryan/ryanminilab1.html", ryanLab = startupStack())
