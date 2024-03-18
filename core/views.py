import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.db.models.functions import Sqrt, Power, Abs
from django.db.models.expressions import ExpressionWrapper
from django.db.models import F, Q, Value, FloatField

from .models import Users


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        body = json.loads(request.body)
        try:
            user = Users(name=body['name'], x=body['x'], y=body['y'])
            user.save()
            response = {'status': 201, 'msg': 'creation success'}
            return JsonResponse(response, status=201)
        except Exception as e:
            response = {'status': 500, 'error': f'Ошибка: {e}'}
            return JsonResponse(response, status=500)


def find_neighbors(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    radius = request.GET.get('radius')
    limit = request.GET.get('limit')
    try:
        queryset = Users.objects.annotate(
            hypotenuse=ExpressionWrapper(
                Sqrt(
                    Abs(Power(Value(x) - F('x'), 2)) +
                    Abs(Power(Value(y) - F('y'), 2))
                ),
                output_field=FloatField()
            )
        )
        filtered_queryset = queryset.filter(Q(hypotenuse__lte=radius))[:int(limit)]
        result = [(user.name, user.hypotenuse) for user in filtered_queryset]
        response = {'status': 200, 'msg': result}
        return JsonResponse(response, status=200)
    except Exception as e:
        response = {'status': 500, 'error': f'Ошибка {e}'}
        return JsonResponse(response, status=500)
