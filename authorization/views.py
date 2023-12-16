from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from authorization.models import User


@csrf_exempt
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    try:
        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            try:
                user = User.objects.get(
                    username=username,
                    password=password
                )
            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_404_NOT_FOUND
                )

            if not user:
                return Response(
                    {'error': 'No such user'},
                    status=status.HTTP_404_NOT_FOUND
                )

            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'token': token.key,
                    'username': token.user.username,
                    'id': token.user_id
                },
                status=status.HTTP_200_OK
            )
        else:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'token': token.key,
                    'username': token.user.username,
                    'id': token.user_id
                },
                status=status.HTTP_200_OK
            )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_404_NOT_FOUND
        )
