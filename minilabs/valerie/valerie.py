from flask import Blueprint, render_template
from flask import request
from minilabs.valerie.valerieminilab import Pigeon

minilabs_valerie = Blueprint('minilabs_valerie', __name__,
                            url_prefix="/valerie",
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@minilabs_valerie.route('/minilab', methods=["GET", "POST"])
def index():
    if request.form == 'POST':
        print(request.method)
        return render_template("valerie/valerieminilab.html", pigeon=Pigeon(200))
    return render_template("valerie/valerieminilab.html")
