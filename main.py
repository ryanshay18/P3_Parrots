from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5001')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('quiz')
def quiz():
    return render_template("quiz.html")


@app.route('about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='3000')
