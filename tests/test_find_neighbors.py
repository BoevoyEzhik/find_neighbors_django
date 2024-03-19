import pytest
from faker import Faker
import json

from django.test.client import Client
from django.urls import reverse
from core.models import Users




@pytest.mark.django_db
@pytest.mark.urls('core.urls')
def test_find_neighbors_status_code_200():
    c = Client()
    data = {'x': 0.3,
            'y': 10,
            'radius': 5,
            'limit': 100}
    url = reverse('find-neighbors')
    response = c.get(url, data, content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.urls('core.urls')
def test_find_neighbors_status_code_500():
    c = Client()
    data = {'x': 0.3,
            'y': 10,
            'radius': 5}
    url = reverse('find-neighbors')
    response = c.get(url, data, content_type='application/json')
    assert response.status_code == 500


@pytest.mark.django_db
@pytest.mark.urls('core.urls')
def test_find_neighbors_correct_data():
    fake = Faker()
    for i in range(5):
        Users.objects.create(name=fake.first_name(), x=i, y=i)
    c = Client()
    data = {'x': 0,
            'y': 0,
            'radius': 5,
            'limit': 100}
    url = reverse('find-neighbors')
    response = c.get(url, data, content_type='application/json')
    content = json.loads(response.content)
    assert len(content['msg']) == 4

