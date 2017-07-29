from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from .models import Hero
import json


def heroList(request):
    if request.method == 'GET':
        return JsonResponse([dict(hero) for hero in Hero.objects.all()], safe=False)
    elif request.method == 'POST':
        name = json.loads(request.body)['name']
        new_hero = Hero(name=name)
        new_hero.save()
        return HttpResponse(status=201) # 'created' response
    else:
        return HttpResponseNotAllowed(['GET', 'POST']) # only GET and POST methods are allowed for this url


def heroDetail(request, hero_id):
    hero_id = int(hero_id)
    if request.method == 'GET':
        return serializers.serialize('json', Hero.objects.get(pk=hero_id))
    elif request.method == 'PUT':
        name = json.loads(request.body)['name']
        hero = Hero.objects.get(id=hero_id)
        hero.name = name
        hero.save()
        return HttpResponse(status=204) # 'No content' response
    elif request.method == 'DELETE':
        hero = Hero.objects.get(id=hero_id)
        hero.delete()
        return HttpResponse(status=204) # 'No content' response
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE']) # only GET and POST methods are allowed for this url

