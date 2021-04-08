from flask import Blueprint, render_template
from flask import request
from minilabs.lola.lolaminilab1 import Math

minilabs_lola = Blueprint('minilabs_lola', __name__,
                          url_prefix="/lola",
                          template_folder="templates",
                          static_folder='static', static_url_path='assets')


@minilabs_lola.route("/minilab", methods=["GET", "POST"])
def lola():
    if request.form == 'POST':
        print(request.method)
        a=int(request.form.get("a"))
        b=int(request.form.get("b"))
        return render_template("lola/lolaminilab1.html", Math=Math(a,b), a=a, b=b, SumDigits=Math.sum_digits, ProductDigits=Math.product_digits, product=Math.product, sum=Math.sum)
    return render_template("lola/lolaminilab1.html")



