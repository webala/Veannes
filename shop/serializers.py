from rest_framework import serializers

class UpdateCartSerializer(serializers.Serializer):
    action = serializers.CharField()
    productId = serializers.IntegerField()