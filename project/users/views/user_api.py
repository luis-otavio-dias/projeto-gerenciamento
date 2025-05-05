from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ..serializers import UserSerializer


@api_view()
def user_api_list(request):
    users = User.objects.all()
    serializer = UserSerializer(instance=users, many=True)

    return Response(serializer.data)


@api_view()
def user_api_detail(request, pk):
    user = get_object_or_404(
        User.objects.filter(pk=pk),
    )
    serializer = UserSerializer(instance=user, many=False)

    return Response(serializer.data)
