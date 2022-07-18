from flask import Flask, jsonify, request
import json
import pickle
import numpy as np
import pandas as pd

from trainig import Response

'''''
app = Flask(__name__)
@app.route("/bot", Method=["POST"])


def response():
   query = dict(request.form)['query']
   result = query + "AAAAAAAAAAA"
   return jsonify({"response" : result})

if __name__ == "__name__":
      app.run(host="0.0.0.0",)


'''''

response = Response()

app = Flask(__name__)
@app.post("/predict")
def predict():
    #text = request.get_json().get("message")
    text = dict(request.form)['message']
    result = response.get_response(text)
    
    message = {"answer": result}
    
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)  
