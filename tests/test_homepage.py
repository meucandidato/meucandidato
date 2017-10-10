# -*- coding: utf-8 -*-


def test_should_return_status_code_200(app):
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200


def test_should_have_the_homepage_content(app):
    with app.test_client() as client:
        response = client.get('/')
        content = str(response.data.decode('utf-8'))

        arq = open('test.html', 'w')
        arq.write(content)

        assert 'Saiba quem é o seu candidato' in content
