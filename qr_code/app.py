from flask import Flask, render_template, request, redirect, url_for, abort
import qrcode

app = Flask(__name__, static_folder='static')


# class Qr_code():
#     def __init__(self, text):
#         self.text = text
#
#     def __repr__(self):
#         return str(dict((key, getattr(self, key)) for key in dir(self) if key not in dir(self.__class__)))
#
#     def generate_image(self, text):
#         qr = pyqrcode.create(text)
#         qr.png('/static/user_gen_qrcode.png', scale=10)


@app.route('/', methods=['GET','POST'])
def main():
    qr_string = ''
    qr_code = None
    if 'user_string' in request.form:
        qr_string = request.form['user_string']
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_code.add_data(qr_string)
        qr_code.make(fit=True)
        img = qr_code.make_image()
        img.save('/static/user_gen_qrcode.png')
    else:
        print('Wrong! It\'s all wrong!!')

    return render_template('main.html', qrcode=qr_code)


if __name__ == '__main__':
    app.run(debug=True)

