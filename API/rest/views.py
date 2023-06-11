import django_filters
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import PerevalFilter
from .models import Users, PerevalAdded
from .serializers import UsersSerializer, PerevalAddedSerializer, PerevalAddedUpdateSerializer


class UserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        if email is not None:
            return self.queryset.filter(user__email=email)
        return self.queryset.none()


class PerevalAddedListView(APIView):
    def get(self, request):
        pereval = PerevalAdded.objects.all()
        serializer = PerevalAddedSerializer(pereval, many=True)
        filterset_class = PerevalFilter
        filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
        return Response(serializer.data)


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalAddedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_data(request, pk):
    try:
        pereval = PerevalAdded.objects.get(pk=pk)
    except PerevalAdded.DoesNotExist:
        return Response(status=404)

    serializer = PerevalAddedSerializer(pereval)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_pereval(request, pk):
    try:
        pereval = PerevalAdded.objects.get(pk=pk)
    except PerevalAdded.DoesNotExist:
        return Response({'state': 0, 'message': 'Pereval not found'}, status=status.HTTP_404_NOT_FOUND)

    if pereval.status != 'new':
        return Response({'state': 0, 'message': 'Pereval status is not "new"'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PerevalAddedUpdateSerializer(pereval, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'state': 1}, status=status.HTTP_200_OK)
    return Response({'state': 0, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


