#this is a simple flask application that runs print Hello World

from flask import Flask


app = Flask(__name__)

@app.route("/")


def hello():
    return "<h2>Vaishnavi Uttarkar Try 3 - Flask Deployment Lab!!!!</h2><hr/>"


app.run(host="0.0.0.0", port=5000)
