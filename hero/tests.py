from django.test import TestCase, Client
from .models import Hero
import json


class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Joker')

        self.client = Client()

    def test_hero_detail_get(self):
        # Test heroDetail with GET request
        response = self.client.get('/api/hero/1')

        data = json.loads(response.content.decode())
        self.assertEqual(data['name'], 'Superman')
        self.assertEqual(response.status_code, 200)

    def test_hero_detail_get_not_found(self):
        # Test heroDetail with GET request
        response = self.client.get('/api/hero/4')

        self.assertEqual(response.status_code, 404)

    def test_hero_detail_post(self):
        # Test heroDetail with POST request
        response = self.client.post('/api/hero/1', json.dumps({'name': 'Spiderman'}), content_type='application/json')

        self.assertEqual(response.status_code, 405)

    def test_hero_detail_put(self):
        # Test heroDetail with PUT request
        response = self.client.put('/api/hero/1', json.dumps({'name': 'Spiderman'}), content_type='application/json')

        self.assertEqual(Hero.objects.get(id=1).name, 'Spiderman')
        self.assertEqual(response.status_code, 204)

    def test_hero_detail_put_not_found(self):
        # Test heroDetail with GET request
        response = self.client.put('/api/hero/4', json.dumps({'name': 'Spiderman'}), content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_hero_detail_delete(self):
        # Test heroDetail with DELETE request
        response = self.client.delete('/api/hero/1')

        self.assertRaises(Hero.DoesNotExist, Hero.objects.get, id=1)
        self.assertEqual(response.status_code, 204)

    def test_hero_detail_delete_not_found(self):
        # Test heroDetail with GET request
        response = self.client.delete('/api/hero/4')

        self.assertEqual(response.status_code, 404)

    def test_hero_list_get(self):
        # Test heroList with GET request
        response = self.client.get('/api/heroes')

        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 3)

    def test_hero_list_post(self):
        # Test heroList with POST request
        response = self.client.post('/api/heroes', json.dumps({'name': 'Spiderman'}), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Hero.objects.get(id=4).name, 'Spiderman')

    def test_hero_list_wrongmethod(self):
        # Test heroList with PUT request
        response = self.client.put('/api/heroes', json.dumps({'name': 'Spiderman'}), content_type='application/json')

        self.assertEqual(response.status_code, 405)

        # Test heroList with DELETE request
        response = self.client.delete('/api/heroes', json.dumps({'name': 'Spiderman'}), content_type='application/json')

        self.assertEqual(response.status_code, 405)

    def test_hero_str(self):
        batman = Hero.objects.get(name='Batman')
        self.assertEqual(str(batman), 'Batman')

    def test_hero_dict(self):
        joker = Hero.objects.get(name='Joker')
        self.assertEqual(dict(joker), {'id': 3, 'name': 'Joker'})

