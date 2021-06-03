from flask import Blueprint, render_template, request
from minilabs.valerie.valerieminilab import Pigeon

from minilabs.valerie.val_bubble_sort import sort

minilabs_valerie = Blueprint('minilabs_valerie', __name__,
                            url_prefix="/valerie",
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@minilabs_valerie.route('/minilab')
def index():
    return render_template("valerie/valerieminilab1.html", pigeon=Pigeon(200))


@minilabs_valerie.route('/minilab/post', methods=['POST'])
def post():

  numbers_str = request.form['numbers']
  sorting_method = '1'

  passes = sort(numbers_str, sorting_method)
  print(passes)

  return render_template("valerie/valerieminilab1-results.html",
                         passes=passes, no_of_passes=len(passes))
