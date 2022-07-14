from flask import Flask, jsonify, request



app = Flask(__name__)
@app.route("/bot", method=["POST"])


def response():
    query = dict(request.form)['query']
    result = query + "AAAAAAAAAAA"
    return jsonify({"response" : result})

if __name__ == "__name__":
    app.run(host="0.0.0.0",)