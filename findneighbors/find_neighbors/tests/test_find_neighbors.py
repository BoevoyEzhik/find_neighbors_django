from django.test import TestCase
from django.urls import reverse
from find_neighbors.models import Users
from faker import Faker


class SomeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(name='Center', x=0, y=0)
        fake = Faker()
        for i in range(5):
            Users.objects.create(name=fake.first_name(), x=i, y=i)

    def test_find_neighbors_status_code_200(self):
        url = reverse('find-neighbors')
        user = Users.objects.get(name='Center')
        data = {'x': user.x,
                'y': user.y,
                'radius': 5,
                'limit': 5}
        response = self.client.get(path=url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_find_neighbors_true_data(self):
        url = reverse('find-neighbors')
        user = Users.objects.get(name='Center')
        data = {'x': user.x,
                'y': user.y,
                'radius': 6,
                'limit': 6}
        response = self.client.get(path=url, data=data, content_type='application/json')
        body = response.json()
        self.assertEqual(len(body['msg']), 6)
