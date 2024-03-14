from find_neighbors.models import Users
from django.db.models import F, Value
from django.db.models.functions import Sqrt, Power, Abs
from django.db.models import FloatField
from django.db.models.expressions import ExpressionWrapper
from django.db.models import Q


def db_create_user(name, x, y):
    user = Users(name=name, x=x, y=y)
    try:
        user.save()
        return False
    except Exception as e:
        return f'ошибка бд {e}'


def db_find_neighbors(x, y, radius, limit):
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
        return [(user.name, user.hypotenuse) for user in filtered_queryset]
    except Exception as e:
        print(e)
        return f'ошибка бд {e}'
