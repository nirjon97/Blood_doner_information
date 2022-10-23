from .models import blood_doner_info
from rest_framework import serializers


class doner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = blood_doner_info
        fields = ['name', 'email', 'phone','age','gender','blood_group','author']