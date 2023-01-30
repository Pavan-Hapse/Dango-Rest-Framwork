from rest_framework import serializers
from watch_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instace, validated_data):
        instace.name = validated_data.get('name', instace.name)
        instace.description = validated_data.get('description', instace.description)
        instace.active = validated_data.get('active', instace.active)
        instace.save()
        return instace


