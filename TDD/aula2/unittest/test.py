# Código da função
def media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# Teste com unittest
import unittest

class TestMedia(unittest.TestCase):
    
    def test_media_valida(self):
        self.assertEqual(media([10, 20, 30]), 20)
        self.assertEqual(media([1, 2, 3, 4]), 2.5)
    
    def test_media_lista_vazia(self):
        self.assertEqual(media([]), 0)

if __name__ == '__main__':
    unittest.main()