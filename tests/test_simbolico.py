import pytest
from ..core.simbolico import derivada, integral
from sympy import symbols, Function, sin, cos, exp, log, sqrt, pi, oo

def test_derivada():
    x = symbols('x')
    y = Function('y')(x)
    z = Function('z')(x)

    # Prueba de derivadas simples
    assert derivada(x**2, x) == 2*x
    assert derivada(sin(x), x) == cos(x)
    assert derivada(cos(x), x) == -sin(x)
    assert derivada(exp(x), x) == exp(x)
    assert derivada(log(x), x) == 1/x
    assert derivada(sqrt(x), x) == 1/(2*sqrt(x))

    # Prueba de derivadas compuestas
    assert derivada(sin(x**2), x) == 2*x*cos(x**2)
    assert derivada(exp(sin(x)), x) == exp(sin(x))*cos(x)
    assert derivada(log(sqrt(x)), x) == 1/(2*x)

    # Prueba de derivadas de funciones definidas por el usuario
    assert derivada(y**2 + z**2, y) == 2*y
    assert derivada(y**2 + z**2, z) == 2*z

def test_integral():
    x = symbols('x')
    y = Function('y')(x)
    z = Function('z')(x)

    # Prueba de integrales simples
    assert integral(x**2, x) == (1/3)*x**3
    assert integral(sin(x), x) == -cos(x)
    assert integral(cos(x), x) == sin(x)
    assert integral(exp(x), x) == exp(x)
    assert integral(log(x), x) == x*log(x) - x
    assert integral(1/sqrt(x), x) == 2*sqrt(x)

    # Prueba de integrales compuestas
    assert integral(sin(x**2), x) == None  # No se puede resolver analíticamente
    assert integral(exp(sin(x)), x) == None  # No se puede resolver analíticamente

    # Prueba de integrales de funciones definidas por el usuario
    assert integral(y**2 + z**2, y) == (1/3)*y**3 + z**2*y
    assert integral(y**2 + z**2, z) == (1/3)*z**3 + y**2*z