import math
from core.constantes_maths import constantes
from gui.funciones import funciones_extra
from core.simbolico import derivada, integral

def evaluar_expresion(expr):
    contexto = {
        **math.__dict__,
        **constantes,
        **funciones_extra,
        "derivada": derivada,
        "integral": integral,
        }
    return eval(expr, {"__builtins__": {}}, contexto)
