from flask import Blueprint, render_template

from minilabs.nick.nickminilab1 import startupStack

nick_blueprint = Blueprint("nick_blueprint", name, static_folder="static", template_folder="templates")


@nick_blueprint.route("/nick")
def nick():
    return render_template("nickminilab1.html", nickLab = startupStack)