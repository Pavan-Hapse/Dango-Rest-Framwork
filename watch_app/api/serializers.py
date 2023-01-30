from rest_framework import serializers
from watch_app.models import Movie


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too Short")


class MovieSerializer(serializers.Serializer):   #
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
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

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")
        else:
            return data

        
"""
    def validate_name(self, value):        #Field level validation
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value"""