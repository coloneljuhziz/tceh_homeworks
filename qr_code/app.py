from flask import Flask, render_template, request, redirect, url_for, abort
import json, pyqrcode

app = Flask(__name__)


class Qrcode():
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return str(dict((key, getattr(self, key)) for key in dir(self) if key not in dir(self.__class__)))


@app.route('/', methods=['POST'])
def main():
    user_string = request.form['user_string']
    return render_template('main.html', user_string = user_string)


if __name__ == '__main__':
    app.run(debug=True)

