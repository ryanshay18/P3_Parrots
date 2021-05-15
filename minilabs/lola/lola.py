from flask import Blueprint, render_template
from flask import request
from minilabs.lola.lolaminilab1 import Math
from minilabs.lola.lolaminilab2 import lolabubblesort

minilabs_lola = Blueprint('minilabs_lola', __name__,
                          url_prefix="/lola",
                          template_folder="templates",
                          static_folder='static', static_url_path='assets')


@minilabs_lola.route("/minilab", methods=["GET", "POST"])
def lola():
    if request.form:
        a = int(request.form.get("a"))
        b = int(request.form.get("b"))
        return render_template("lola/lolaminilab1.html", math=Math(a,b))
    return render_template("lola/lolaminilab1.html",math=Math(0,0))

@minilabs_lola.route("/minilab", methods=['GET', 'POST'])
def lola2():
    x = 0
    list = ""
    if request.form == 'POST':
        value = request.form['list']
        y = lolabubblesort
        x = y.x_original(value)
        list = y.bubbleSort(value)
    return render_template("/lola/lolaminilab1.html", x=x, list=list)


