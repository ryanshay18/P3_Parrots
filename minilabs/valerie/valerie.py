from flask import Blueprint, render_template

from minilabs.valerie.valerieminilab import Pigeon

minilabs_valerie_bp = Blueprint('minilabs_valerie', __name__,
                                template_folder='templates',
                                static_folder='static', static_url_path='assets')


@minilabs_valerie_bp.route('/')
def index():
    return render_template("valerietemplate.html", pigeon=Pigeon(200))
