from utils import es_email_correcto


def test_retorna_true_si_recibe_email_con_formato_correcto():
    assert es_email_correcto("juan@email.com") is True


def test_retorna_false_si_recibe_email_con_formato_incorrecto():
    assert es_email_correcto("hola") is False
