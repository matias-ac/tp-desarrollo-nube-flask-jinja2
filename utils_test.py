import unittest

from utils import es_email_correcto


class EsEmailCorrectoTests(unittest.TestCase):
    def test_retorna_true_si_recibe_email_con_formato_correcto(self):
        self.assertEqual(es_email_correcto("juan@email.com"), True)

    def test_retorna_false_si_recibe_email_con_formato_incorrecto(self):
        self.assertEqual(es_email_correcto("hola"), False)


if __name__ == "__main__":
    unittest.main()
