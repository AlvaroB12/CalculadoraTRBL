from sympy import symbols, diff, integrate, sympify

x = symbols('x')

def derivada(expr):
    return diff(sympify(expr), x)

def integral(expr):
    return integrate(sympify(expr), x)
 