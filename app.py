from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    qr_image = None

    if request.method == 'POST':

        url = request.form['url']

        qr = qrcode.make(url)

        buffer = io.BytesIO()

        qr.save(buffer, format="PNG")

        img_base64 = base64.b64encode(
            buffer.getvalue()
        ).decode()

        qr_image = f"data:image/png;base64,{img_base64}"

    return render_template(
        'index.html',
        qr_image=qr_image
    )

if __name__ == '__main__':
    app.run(debug=True)