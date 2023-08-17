from django.test import TestCase
from django.urls import reverse
import json

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

class Weather_data_tests(TestCase):

    def test_city(self):
        city='San Francisco'
        url=reverse('weather',args=[city])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json()['data'],weather_data[city])

    def test_invalid(self):
        city='Mumbai'
        url=reverse('weather',args=[city])
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,404)
        self.assertEqual(resp.json()['data'],"city not found")

    def test_create(self):
        url=reverse('create')
        resp=self.client.post(url,json.dumps({"city":"Mumbai","temperature":25,"weather":"Cloudy"}),content_type='application/json')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(resp.json()['data'],"data posted succesfully")