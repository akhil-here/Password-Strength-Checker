from flask import Flask, render_template, request
from pass_check import *

app = Flask(__name__)


@app.route("/")
def display():
    return render_template('index.html')


@app.route("/check", methods=['POST'])
def check_strength(sum=sum):
    if request.method == 'POST':
        password = request.form['pwd']
        x.append(password)
        ip = vectorizer.fit_transform(x)
        switcher = {
            0: "Weak password!!!",
            1: "Moderate password!!!",
            2: "Strong password!!!",
        }
        ans = m.predict(ip)
        return render_template('index.html', sum=switcher.get(ans[-1], " "))

    else:
        return render_template('index.html', sum=" ")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
