from rest_framework import serializers

class CodeGenerationSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True)
    filename = serializers.CharField(required=True)
