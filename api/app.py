# api/app.py

from flask import Flask, request, jsonify
from ..core.parser import evaluar_expresion
from ..core.simbolico import derivada, integral

app = Flask(__name__)

@app.route('/api/calculate', methods=['POST'])
def calcular():
    data = request.get_json()
    expresion = data.get("expresion", "")
    try:
        resultado = evaluar_expresion(expresion)
        return jsonify({"resultado": str(resultado)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/derivar', methods=['POST'])
def derivada():
    data = request.get_json()
    expresion = data.get("expresion", "")
    variable = data.get("variable", "x")
    try:
        resultado = derivada(expresion, variable)
        return jsonify({"resultado": str(resultado)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/integrar', methods=['POST'])
def integral():
    data = request.get_json()
    expresion = data.get("expresion", "")
    variable = data.get("variable", "x")
    try:
        resultado = integral
        (expresion, variable)
        return jsonify({"resultado": str(resultado)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
 