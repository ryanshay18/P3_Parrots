from flask import Blueprint, render_template, request

from minilabs.ryan.ryanminilab import startupStack

minilabs_ryan = Blueprint("minilabs_ryan", __name__,
                          url_prefix="/ryan",
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@minilabs_ryan.route("/minilab")
def ryan():
    return render_template("ryan/ryanminilab1.html", ideaStack = startupStack())

@app.route('/ideaGiven', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        minilab1_data = request.form
        return render_template('ideGiven.html',minilab1_data = minilab1_data)
