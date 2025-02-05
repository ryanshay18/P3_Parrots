# import requests
from flask import Flask, render_template, request

from quiz import quiz_data

from query import query_colleges
from entertainment_api import query_movies

from minilabs.valerie.valerie import minilabs_valerie
from minilabs.lola.lola import minilabs_lola
from minilabs.ryan.ryan import minilabs_ryan
from minilabs.michael.michael import minilabs_michael
from minilabs.nick.nick import minilabs_nick

app = Flask(__name__)
app.register_blueprint(minilabs_valerie)
app.register_blueprint(minilabs_lola)
app.register_blueprint(minilabs_ryan)
app.register_blueprint(minilabs_nick)
app.register_blueprint(minilabs_michael)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/easteregg/')
def easteregg():
    return render_template("easteregg.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html",
                           data=quiz_data(),
                           question_index=0,
                           answers='{}')


@app.route('/minilabs')
def about():
    return render_template("minilabs.html")


@app.route('/howitsmade')
def howitsmade():
    return render_template("howitsmade.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")


@app.route('/responses/')
def responses():
    return render_template("responses.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/next', methods=['POST'])
def next_question():
    print(request.form['answer'])
    print(request.form['answers'])
    print(request.form['next_question'])
    return render_template("quiz.html",
                           data=quiz_data(),
                           question_index=int(request.form['next_question']),
                           answers=request.form['answers'])


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form['answers'])
    movies = query_movies(request.form['answers'])
    return render_template("results.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8080')
