import pytest
from ..core.constantes_maths import constantes

def test_constantes():
    # Test if the constantes module is imported correctly
    assert constantes is not None, "Constantes module should be imported correctly"

    # Test if the constants are defined
    assert hasattr(constantes, 'pi'), "Constante pi should be defined"
    assert hasattr(constantes, 'e'), "Constante e should be defined"
    assert hasattr(constantes, 'phi'), "Constante phi should be defined"
    assert hasattr(constantes, 'tau'), "Constante tau should be defined"
    assert hasattr(constantes, 'g'), "Constante g should be defined"
    assert hasattr(constantes, 'c'), "Constante c should be defined"
    assert hasattr(constantes, 'h'), "Constante h should be defined"