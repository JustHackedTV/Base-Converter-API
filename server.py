from flask import Flask
from converter import decimalParaBase, readConfig, baseParaDecimal

app = Flask("Converter API")

@app.route("/")
def home():
    return None

@app.route("/<numero>/<base1>/<base2>")
def api_call_db(numero, base1, base2):
    if (base1 == "1" or base2 == "1"): return "Base 1 não é aceita"
    try:
        return decimalParaBase(baseParaDecimal(numero, base1), base2, readConfig("config.txt"))
    except ZeroDivisionError:
        return "Base 0"

if __name__ == "__main__":
    app.run(debug=True)
