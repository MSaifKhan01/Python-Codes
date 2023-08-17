from django.test import TestCase,Client
import json
from .models import Menu

class MenuTests(TestCase):
    def setUp(self):
        self.client=Client()

    def test_add_dish(self):
        data = {"dishname": "dal", "price": 100, "available": "yes"}
        resp = self.client.post("/crud/createmenu", data, content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Menu.objects.count(), 1)

    


    def test_get_route(self):
        url = '/crud/getmenu'

        response = self.client.get(url)
        print(response)

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode('utf-8'))
        print(response_data)
        data_expected = '[]'
        self.assertEqual(response_data, data_expected)     

    def test_Update(self):
        menu=Menu.objects.create(dishname="dal",price=100,available="no")
        data={"available":"no"}
        resp=self.client.patch(f"/crud/updatemenu/{menu.id}",data,content_type="application/json")
        self.assertEqual(resp.status_code,200)
        self.assertEqual(menu.available,"no")
    
    def test_Delete(self):
        menu=Menu.objects.create(dishname="dal",price=100,available="no")
        resp=self.client.delete(f"/crud/deletemenu/{menu.id}")
        self.assertEqual(resp.status_code,200)
        self.assertEqual(Menu.objects.count(),0)