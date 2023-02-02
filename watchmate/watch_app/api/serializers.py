from rest_framework import serializers
from watch_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):  # We can add the reviews through this serializer
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        #fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"  # This process is shows all fields of individual object

        # fields = ['id', 'name', 'description']  # This process is shows only 3 fields of individual object
        # exclude = ['active']                    # It will exclude active field and shows rest of the fields


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True)  # This method will return the name of watchlist name

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    #
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.validationError("Title and Description should be different")
    #     else:
    #         return data
    #
    # def validate_name(self, value):                     #Field level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too Short")
    #     else:
    #         return value

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
