import json
from flask import Flask, jsonify, request, render_template,  make_response
from flask_qrcode import QRcode

app = Flask(__name__)
app.config["DEBUG"] = True

# Add qr code genrator
QRcode(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', to_encode="NEED_TO_FIX_THIS")

# Run app
app.run(host='0.0.0.0')