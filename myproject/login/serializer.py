from rest_framework import serializers
class listUserSerializer(serializers.Serializer):
        name = serializers.CharField()
        id = serializers.IntegerField()
        email =serializers.EmailField()
