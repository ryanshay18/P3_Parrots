# import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


@app.route('/about')
def about():
    return render_template("about.html")

"""
@app.route('/api/')
def api():
    headers = {
        'x-rapidapi-key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
        'x-rapidapi-host': "university-college-list-and-rankings.p.rapidapi.com"
    }
    url = "https://university-college-list-and-rankings.p.rapidapi.com/api/top-universities/europe"
    response = requests.request("GET", url, headers=headers)
    setup = response.json()[0]['setup']
    college = response.json()[0]['college']
    return render_template('colleges.html', setup = setup, college = college)
    #print(response.text)
"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='3000')
