from . import models
from rest_framework import serializers

class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Testmodel
        fields='__all__'