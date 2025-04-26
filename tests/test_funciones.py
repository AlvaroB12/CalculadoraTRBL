import pytest
from gui.funciones import * # Importa todas las funciones del módulo funciones.py

def test_deg():
    assert deg(0) == 0
    assert deg(90) == 1.5707963267948966
    assert deg(180) == 3.141592653589793
    assert deg(270) == 4.71238898038469
    assert deg(360) == 6.283185307179586
    assert deg(-90) == -1.5707963267948966
    assert deg(-180) == -3.141592653589793
    assert deg(-270) == -4.71238898038469
    assert deg(-360) == -6.283185307179586

def test_rad():
    assert rad(0) == 0
    assert rad(1.5707963267948966) == 90
    assert rad(3.141592653589793) == 180
    assert rad(4.71238898038469) == 270
    assert rad(6.283185307179586) == 360
    assert rad(-1.5707963267948966) == -90
    assert rad(-3.141592653589793) == -180
    assert rad(-4.71238898038469) == -270
    assert rad(-6.283185307179586) == -360

def test_cuadrado():
    assert cuadrado(2) == 4
    assert cuadrado(-2) == 4
    assert cuadrado(0) == 0
    assert cuadrado(1.5) == 2.25
    assert cuadrado(-1.5) == 2.25
    assert cuadrado(3.14) == 9.8596

def test_cubo():
    assert cubo(2) == 8
    assert cubo(-2) == -8
    assert cubo(0) == 0
    assert cubo(1.5) == 3.375
    assert cubo(-1.5) == -3.375
    assert cubo(3.14) == 31.003144000000002

