from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def display():
    return render_template('index.html')


@app.route("/check", methods=['POST'])
def check_strength(strength=strength):
    if request.method == 'POST':
        password = request.form['pwd']
        return render_template('index.html', strength="Strong!!")
    else:
        return render_template('index.html', strength=" ")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
