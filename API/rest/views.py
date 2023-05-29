from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users, Coords, Images, PerevalAdded, Level
from .serializers import UsersSerializer, CoordsSerializer, ImageSerializer, PerevalAddedSerializer, LevelSerializer


class UserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsListView(generics.ListAPIView):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class ImageListView(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class PerevalAddedListView(APIView):
    def get(self, request):
        pereval = PerevalAdded.objects.all()
        serializer = PerevalAddedSerializer(pereval, many=True)
        return Response(serializer.data)


class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer