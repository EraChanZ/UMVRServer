from rest_framework import serializers
from court.models import Court

class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['name', 'address_row', 'latitude', 'longitude', 'nearest_metro', 'is_free']

class CourtSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['name', 'address_row', 'latitude', 'longitude', 'nearest_metro', 'is_free', 'main_image']
