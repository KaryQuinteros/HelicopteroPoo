from Helicoptero import Helicoptero
import pytest

def test_inicializacion_componentes():
    helicoptero_militar = Helicoptero("AS350", "Azul", 100)
    assert isinstance(helicoptero_militar, Helicoptero)

def test_inicializacion():
    helicoptero_militar = Helicoptero("AS350", "Azul", 100)
    assert helicoptero_militar.modelo == "AS350"
    assert helicoptero_militar.color == "Azul"
    assert helicoptero_militar.combustible_inicial == 100
    assert helicoptero_militar.estado == False

def test_str():
    helicoptero_militar = Helicoptero("AS350", "Azul", 100)
    assert str(helicoptero_militar) == "Su modelo de helicoptero AS350 su color es Azul y su combistible marca 100"

def test_setter_modelo():
    helicoptero_militar = Helicoptero("AS350", "Azul", 100)
    helicoptero_militar.modelo = "AH-1ZViper"
    assert helicoptero_militar.modelo == "AH-1ZViper"

def test_encender_helicoptero():
    helicoptero_militar = Helicoptero("AS350", "Azul", 100)
    helicoptero_militar.encender_helicoptero()
    assert helicoptero_militar.estado == True
    with pytest.raises(ValueError, match= "El helicoptero esta encendido"):
        helicoptero_militar.encender_helicoptero()

def test_apagar_helicoptero():
    helicoptero_militar = Helicoptero("AS350", "Azul", 100)
    helicoptero_militar.encender_helicoptero()
    helicoptero_militar.apagar_helicoptero()
    assert helicoptero_militar.estado == False
    with pytest.raises(ValueError):
        helicoptero_militar.apagar_helicoptero()