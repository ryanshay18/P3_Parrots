from flask import Blueprint, render_template, request

from minilabs.ryan.ryanminilab import startupStack

from minilabs.ryan.ryan_bubble_sort import bubbleSort

minilabs_ryan = Blueprint("minilabs_ryan", __name__,
                          url_prefix="/ryan",
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@minilabs_ryan.route("/minilab", methods=['POST', 'GET'])
def ryan():
    return render_template("ryan/ryanminilab1.html", ideaStack=startupStack())


def bubble_data():
    bdata = request.form['text']
    return bubbleSort(bdata)

"""
@minilabs_ryan.route('/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        minilab1_data = request.form
        return render_template('ideGiven.html', minilab1_data=minilab1_data)
"""
"""
def bubble_data():
    bdata = request.form['text']
    return bubbleSort(bdata)

app.jinja_env.globals.update(bubble_data=bubble_data)
"""