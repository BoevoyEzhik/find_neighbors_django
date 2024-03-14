import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from find_neighbors.db_utils import db_find_neighbors, db_create_user


def index(request):
    return HttpResponse('Hello, neighbor!')


def find_neighbors(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    radius = request.GET.get('radius')
    limit = request.GET.get('limit')
    db_result = db_find_neighbors(x, y, radius, limit)
    if type(db_result) is str:
        response = {'status': 500, 'error': db_result}
        return JsonResponse(response, status=500)
    response = {'status': 200, 'msg': db_result}
    return JsonResponse(response, status=200)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        body = json.loads(request.body)
        db_result = db_create_user(body['name'], body['x'], body['y'])
        if db_result:
            response = {'status': 500, 'error': db_result}
            return JsonResponse(response, status=500)
        response = {'status': 201, 'msg': 'creation success'}
        return JsonResponse(response, status=201)
    elif request.method == "GET":
        response = {'status': 200, 'msg': 'ok'}
        return JsonResponse(response, status=200)
