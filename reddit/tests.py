# Create your tests here.
from django.test import TestCase
from django.test import Client


class Test(TestCase):
    def setUp(self) :
        self.client = Client()
    def test_details(self):
        response = self.client.get('/r/news/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/r/news?query=germany')
        self.assertRedirects(response, '/r/news/?query=germany', status_code=301, target_status_code=200)

        response = self.client.get('/r/news/?query=usa')
        self.assertEqual(response.status_code, 200)
