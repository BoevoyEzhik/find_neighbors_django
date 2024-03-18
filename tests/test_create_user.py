import pytest

from django.test.client import Client
from django.urls import reverse

from core.models import Users


@pytest.mark.django_db
@pytest.mark.urls('core.urls')
def test_create_user_status_code_201():
    c = Client()
    data = {'name': 'Aleks',
            'x': '0.3',
            'y': '10'}
    url = reverse('create-user')
    response = c.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
@pytest.mark.urls('core.urls')
def test_create_user_status_code_500():
    c = Client()
    data = {'name': 'Aleks',
            'x': 'qwe',
            'y': '10'}
    url = reverse('create-user')
    response = c.post(url, data, content_type='application/json')
    assert response.status_code == 500


@pytest.mark.django_db
@pytest.mark.urls('core.urls')
def test_create_user_user_added():
    c = Client()
    data = {'name': 'Aleks',
            'x': 0.3,
            'y': 10}
    url = reverse('create-user')
    response = c.post(url, data, content_type='application/json')
    user = Users.objects.get(name=data['name'])
    assert user.name == data['name']
    assert user.x == data['x']
    assert user.y == data['y']
