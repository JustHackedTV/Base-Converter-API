from flask import Flask, jsonify, request
from converter import decimalParaBase, readConfig

app = Flask(__name__)

@app.route("/<numero>/<base>")
def home(numero, base):
    return decimalParaBase(numero, base, readConfig("config.txt"))

if __name__ == "__main__":
    app.run(debug=True)