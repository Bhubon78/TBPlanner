#import Flask
from flask import Flask, make_response, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return make_response(jsonify({"message": "Welcome to the Budget Travel Planner API"}), 200)

if __name__ == "__main__":
    app.run(debug=True)