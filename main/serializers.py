from rest_framework import serializers
from .models import Scripts, Sessions, Broadcasts, Syllabus

class ScriptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripts
        fields = '__all__'

class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = '__all__'

class BroadcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcasts
        fields = '__all__'

class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'
