from bs4 import BeautifulSoup

from app import app


def test_renderiza_el_formulario_con_status_200():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_renderiza_el_formulario_con_titulo():
    tester = app.test_client()
    response = tester.get("/")
    assert "Formulario de registro" in response.text


def test_formulario_contiene_input_nombre():
    tester = app.test_client()
    response = tester.get("/")
    soup = BeautifulSoup(response.text, "html.parser")

    input_nombre = soup.find("input", attrs={"name": "nombre"})

    assert input_nombre is not None


def test_formulario_contiene_input_email():
    tester = app.test_client()
    response = tester.get("/")
    soup = BeautifulSoup(response.text, "html.parser")

    input_email = soup.find("input", attrs={"name": "email"})

    assert input_email is not None


def test_formulario_contiene_input_edad_numerico():
    tester = app.test_client()
    response = tester.get("/")
    soup = BeautifulSoup(response.text, "html.parser")

    input_edad = soup.find("input", attrs={"name": "edad"})

    assert input_edad is not None
    assert input_edad["type"] == "number"


def test_formulario_contiene_text_area():
    tester = app.test_client()
    response = tester.get("/")
    soup = BeautifulSoup(response.text, "html.parser")

    text_area_comentarios = soup.find("textarea", attrs={"name": "comentarios"})

    assert text_area_comentarios is not None
