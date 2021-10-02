from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404


from app.api.serializers import BasicModelSerializer
from app.models import BasicModel


#  CV related views

class BasicModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = BasicModel.objects.all()
    serializer_class = BasicModelSerializer
