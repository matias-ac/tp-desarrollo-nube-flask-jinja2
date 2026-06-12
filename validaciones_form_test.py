from validaciones_form import (
    eliminar_espacios_duplicados,
    es_email_correcto,
    es_nombre_correcto,
)


def test_retorna_false_si_recibe_email_con_formato_incorrecto():
    assert es_email_correcto("hola") is False


def test_retorna_true_si_recibe_email_con_formato_correcto():
    assert es_email_correcto("juan@email.com") is True


def test_retorna_false_si_nombre_contiene_caracteres_no_alfabeticos():
    assert es_nombre_correcto("Ju4n Carlo$") is False


def test_retorna_false_si_nombre_esta_vacio():
    assert es_nombre_correcto("   ") is False


def test_retorna_true_si_nombre_recibido_solo_contiene_caracteres_alfabeticos():
    assert es_nombre_correcto("Juan Carlos") is True


def test_elimina_espacios_duplicados():
    assert eliminar_espacios_duplicados("  Juan       Carlos    ") == "Juan Carlos"
    assert eliminar_espacios_duplicados("   123    456    ") == "123 456"
