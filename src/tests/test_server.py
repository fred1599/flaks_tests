from printoptim import app


def test_home():
    tester = app.test_client()
    assert tester.application.name == "printoptim"
    response = tester.get('/', content_type='html/text')
    assert response.data == b"hello"
    assert response.status_code == 200
