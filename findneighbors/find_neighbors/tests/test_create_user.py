from django.test import TestCase
from django.urls import reverse
from find_neighbors.models import Users


class SomeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(name='Name', x=20, y=20)

    def test_create_user_get(self):
        url = reverse('create-user')
        response = self.client.get(path=url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_user_post_status_code_201(self):
        self.user = Users.objects.get(name='Name')
        url = reverse('create-user')
        data = {'name': self.user.name, 'x': self.user.x, 'y': self.user.y}
        response = self.client.post(path=url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_user_successful_db_creation(self):
        self.user = Users.objects.get(name='Name')
        url = reverse('create-user')
        data = {'name': self.user.name, 'x': self.user.x, 'y': self.user.y}
        response = self.client.post(path=url, data=data, content_type='application/json')
        self.assertEqual(self.user.name, 'Name')

    def test_create_user_post_negative(self):
        self.user = Users.objects.create(name='Name', x=20, y=20)
        url = reverse('create-user')
        data = {'name': 3, 'x': 'we', 'y': 20}
        response = self.client.post(path=url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 500)
