import pytest
from fila import Fila

def test_enfileirar():
    f = Fila()
    f.enfileirar(1)
    assert f.frente() == 1

def test_desenfileirar():
    f = Fila()
    f.enfileirar(1)
    assert f.desenfileirar() == 1
    assert f.esta_vazia()

def test_frente():
    f = Fila()
    f.enfileirar("A")
    assert f.frente() == "A"

def test_tamanho():
    f = Fila()
    f.enfileirar(1)
    f.enfileirar(2)
    assert f.tamanho() == 2

def test_excecao_fila_vazia():
    f = Fila()
    with pytest.raises(IndexError):
        f.desenfileirar()

