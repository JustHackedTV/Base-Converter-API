from flask import Flask, jsonify, request
from converter import decimalParaBase, readConfig

app = Flask(__name__)

@app.route("/<numero>/<base>")
def home(numero, base):
    if (base == "1"): return "Base 1 não é aceita"
    try:
        return decimalParaBase(numero, base, readConfig("config.txt"))
    except ZeroDivisionError:
        return "Base 0"

if __name__ == "__main__":
    app.run(debug=True)
