# Código da função (mesmo do exemplo anterior)
def media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# Teste com pytest
def test_media_valida():
    assert media([10, 20, 30]) == 20
    assert media([1, 2, 3, 4]) == 2.5

def test_media_lista_vazia():
    assert media([]) == 0