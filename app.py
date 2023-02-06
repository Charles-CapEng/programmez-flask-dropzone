#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import os

# initialize dropzone
app = Flask(__name__)
dropzone = Dropzone(app)

@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    return render_template("index.html")

@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('uploadsFolder', f.filename))

    return 'upload template'

if __name__ == "main":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)