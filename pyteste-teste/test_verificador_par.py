# arquivo de teste: test_verificador_par.py
from verificador_par import eh_par

def test_eh_par():
    # Testa números pares
    assert eh_par(2) == True
    assert eh_par(0) == True
    assert eh_par(-4) == True

    # Testa números ímpares
    assert eh_par(3) == False
    assert eh_par(7) == False
    assert eh_par(-1) == False

    # Testa zero
    assert eh_par(0) == True

    # Testa números grandes
    assert eh_par(10**6) == True
    assert eh_par(10**5 + 1) == False