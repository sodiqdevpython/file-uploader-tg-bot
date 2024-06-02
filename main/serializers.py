from rest_framework import serializers
from .models import mainData, DocsData, DocsData2, DocsData3, DocsData4, DocsData5, DocsData6

class mainDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainData
        fields = '__all__'

class DocsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocsData
        fields = '__all__'

class DocsData2Serializer(serializers.ModelSerializer):
    class Meta:
        model = DocsData2
        fields = '__all__'

class DocsData3Serializer(serializers.ModelSerializer):
    class Meta:
        model = DocsData3
        fields = '__all__'

class DocsData4Serializer(serializers.ModelSerializer):
    class Meta:
        model = DocsData4
        fields = '__all__'

class DocsData5Serializer(serializers.ModelSerializer):
    class Meta:
        model = DocsData5
        fields = '__all__'

class DocsData6Serializer(serializers.ModelSerializer):
    class Meta:
        model = DocsData6
        fields = '__all__'
