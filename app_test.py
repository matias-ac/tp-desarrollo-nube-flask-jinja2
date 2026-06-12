from app import app


def test_renderiza_el_formulario_con_status_200():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_renderiza_el_formulario_con_titulo():
    tester = app.test_client()
    response = tester.get("/")
    assert "Formulario de registro" in response.text
