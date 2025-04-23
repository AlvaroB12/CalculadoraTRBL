import math

def rad(grados): return math.radians(grados)
def deg(radianes): return math.degrees(radianes)
def cuadrado(x): return x ** 2
def cubo(x): return x ** 3

funciones_extra = {
    "rad": rad,
    "deg": deg,
    "cuadrado": cuadrado,
    "cubo": cubo,
}
