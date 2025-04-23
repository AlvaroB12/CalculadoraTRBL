import pytest
from ..core.historial import Historial

def test_historial_initialization():
    # Test the initialization of the Historial class
    historial = Historial()
    assert isinstance(historial, Historial)
    assert historial.historial == []  # Check if the historial is initialized as an empty list

def test_agregar_operacion():
    h = Historial()
    h.agregar("2 + 2 = 4")
    assert h.obtener_ultimo() == "2 + 2 = 4"
