from rest_framework import serializers
from .models import Tech


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ["id", "name", "url", "progress"]

    def create(self, validated_data):
        return Tech.objects.create(**validated_data)
