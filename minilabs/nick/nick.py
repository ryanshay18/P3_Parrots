from flask import Blueprint, render_template

from minilabs.nick.nickminilab1 import random

minilabs_nick = Blueprint('minilabs_nick', __name__,
                            url_prefix="/nick",
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@minilabs_nick.route("/minilab")
def nick():
    return render_template("nick/nickminilab1.html", random=random(90))