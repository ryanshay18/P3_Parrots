from flask import Blueprint, render_template

from minilabs.valerie.valerieminilab import Pigeon

minilabs_valerie = Blueprint('minilabs_valerie', __name__,
                            url_prefix="/valerie",
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@minilabs_valerie.route('/minilab')
def index():
    return render_template("valerie/valerieminilab1.html", pigeon=Pigeon(200))
