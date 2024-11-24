from rest_framework import serializers
from olx_clone_api.models import BikeModel

class BikeSerializer(serializers.ModelSerializer):
    post_date = serializers.DateField(read_only=True)
    is_negotiable = serializers.BooleanField(read_only=True)
    class Meta:
        model=BikeModel
        fields='__all__'