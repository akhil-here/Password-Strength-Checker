from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/intro")
def intro():
    return 'Hello Akhil!!!'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
