import re


def es_email_correcto(email: str):
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False


def eliminar_espacios_duplicados(texto: str):
    palabras_del_texto = texto.split()
    texto_formateado = " ".join(palabras_del_texto)
    return texto_formateado


def es_nombre_correcto(nombre: str):
    nombre_ingresado = eliminar_espacios_duplicados(nombre)
    if not nombre_ingresado.replace(" ", "").isalpha():
        return False
    return True


def es_edad_correcta(edad):
    edad_ingresada: int
    try:
        edad_ingresada = int(edad)
        if edad_ingresada < 1:
            return False
    except ValueError:
        return False
    return True
