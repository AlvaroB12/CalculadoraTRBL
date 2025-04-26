import pytest
from calculadora.simbolico import derivada, integral
from sympy import symbols, Function, sin, cos, exp, log, sqrt, pi, oo

def test_derivada():
    x = symbols('x')
    y = Function('y')(x)
    z = Function('z')(x)

    # Prueba de derivadas simples
    assert derivada(x**2) == 2*x
    assert derivada(sin(x)) == cos(x)
    assert derivada(cos(x)) == -sin(x)
    assert derivada(exp(x)) == exp(x)
    assert derivada(log(x)) == 1/x
    assert derivada(sqrt(x)) == 1/(2*sqrt(x))

    # Prueba de derivadas compuestas
    assert derivada(sin(x**2)) == 2*x*cos(x**2)
    assert derivada(log(sqrt(x)), x) == 1/(2*x)

def test_integral():
    x = symbols('x')
    y = Function('y')(x)
    z = Function('z')(x)

    # Prueba de integrales simples
    assert integral(x**2) == (1/3)*x**3
    assert integral(sin(x)) == -cos(x)
    assert integral(cos(x)) == sin(x)
    assert integral(exp(x)) == exp(x)
    assert integral(log(x)) == x*log(x) - x
    assert integral(1/sqrt(x)) == 2*sqrt(x)

    # Prueba de integrales compuestas
    assert integral(sin(x**2)) == None  # No se puede resolver analíticamente
    assert integral(exp(sin(x))) == None  # No se puede resolver analíticamente
