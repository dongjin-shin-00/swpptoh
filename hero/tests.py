from django.test import TestCase
from .models import Hero


class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Joker')

    def test_hero_str(self):
        batman = Hero.objects.get(name='Batman')
        self.assertEqual(str(batman), 'Batman')

    def test_hero_dict(self):
        joker = Hero.objects.get(name='Joker')
        self.assertEqual(dict(joker), {'id': 3, 'name': 'Joker'})

