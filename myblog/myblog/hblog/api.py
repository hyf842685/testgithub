from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Topmenu


class Topmenuxuliehua(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Topmenu
        fields = '__all__'



@api_view(['GET'])
def index(request):
    topmenu = Topmenu.objects.all()
    topmenuData = Topmenuxuliehua(topmenu, many=True)
    return Response({'topmenu': topmenuData.data})
