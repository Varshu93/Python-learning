from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/2"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
