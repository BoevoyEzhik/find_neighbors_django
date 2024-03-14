from django.test import TestCase
from django.urls import reverse
from find_neighbors.models import Users


class SomeTest(TestCase):

    def test_create_user_get(self):
        url = reverse('create-user')
        response = self.client.get(path=url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_user_post_status_code_201(self):
        url = reverse('create-user')
        data = {'name': 'test_user', 'x': -23.5, 'y': 5}
        response = self.client.post(path=url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_user_successful_db_creation(self):
        url = reverse('create-user')
        data = {'name': 'test_user2', 'x': -23.5, 'y': 5}
        response = self.client.post(path=url, data=data, content_type='application/json')
        user = Users.objects.get(name='test_user2')
        self.assertEqual(user.name, 'test_user2')

    def test_create_user_post_negative(self):
        url = reverse('create-user')
        data = {'name': 3, 'x': 'we', 'y': 20}
        response = self.client.post(path=url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 500)
