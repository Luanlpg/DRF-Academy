import unittest
from main import cpf, telefone

class TestCPF(unittest.TestCase):
    
    def test_cpf_tamanho(self):
        try:
            cpf('1234567890')
        except Exception as error:
            self.assertEqual(str(error), "CPF Inválido")
        self.assertEqual(len(cpf('12345678901')), 14)    
        
    
    def test_cpf_success(self):
        self.assertEqual(cpf('12345678900'), '123.456.789-00')


class TestTelefone(unittest.TestCase):
    
    def test_tel_tamanho(self):
        try:
            telefone('1196465869')
        except Exception as error:
            self.assertEqual(str(error), "Telefone Inválido")
        self.assertEqual(len(telefone('11964658699')), 14)
    
    def test_tel_success(self):
        self.assertEqual(telefone('11964658699'), '(11)96465-8699')

if __name__ == '__main__':
    unittest.main()