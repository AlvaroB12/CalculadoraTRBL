import math
from calculadora.constantes_maths import constantes
from calculadora.funciones import funciones_extra
from calculadora.simbolico import derivada, integral

def evaluar_expresion(expr):
    contexto = {
        **math.__dict__,
        **constantes,
        **funciones_extra,
        "derivada": derivada,
        "integral": integral,
        }
    return eval(expr, {"__builtins__": {}}, contexto)
