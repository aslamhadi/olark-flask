import os
import time
import simplejson
from pprint import pprint
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test')
def hello():
    return 'Hello World!'


@app.route("/", methods=["POST"])
def index():
    data = simplejson.loads(request.form['data'])
    print data
    return jsonify(integrationUrl="https://still-tor-4534.herokuapp.com/%s/" % data['id'])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)
