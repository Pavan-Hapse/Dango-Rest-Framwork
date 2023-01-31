from rest_framework import serializers
from watch_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"  # This process is shows all fields of individual object

        # fields = ['id', 'name', 'description']  # This process is shows only 3 fields of individual object
        # exclude = ['active']                    # It will exclude active field and shows rest of the fields

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.validationError("Title and Description should be different")
        else:
            return data

    def validate_name(self, value):                     #Field level validation
        if len(value) < 2:
            raise serializers.ValidationError("Name is too Short")
        else:
            return value




# def name_length(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('desciption', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#
#