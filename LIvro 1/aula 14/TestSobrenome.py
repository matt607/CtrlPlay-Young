import unittest
from sobrenome import SobrenomeNaOrdem

class NomeTest(unittest.TestCase):

    def test_sobrenomeNaOrdem(self):

        nomeCompleto = SobrenomeNaOrdem ('João', 'Madureira', 'Silva')
        self.assertEqual(nomeCompleto, 'João Madureira Silva')
unittest.main(argv=[''], exit=False)
