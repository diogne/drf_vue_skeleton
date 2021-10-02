from rest_framework import serializers
from app.models import BasicModel

class BasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicModel
        fields = "__all__"
