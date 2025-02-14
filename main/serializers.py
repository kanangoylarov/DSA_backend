from rest_framework import serializers
from .models import Scripts, Sessions, Broadcasts, Syllabus

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

class ScriptsSerializer(serializers.ModelSerializer):
    sessions = SessionsSerializer(many=True, read_only=True)
    broadcast = BroadcastsSerializer(read_only=True)
    syllabus = SyllabusSerializer(many=True, read_only=True)


    class Meta:
        model = Scripts
        fields = '__all__'

    def get_broadcast(self, obj):
        if hasattr(obj, 'broadcast'):
            return BroadcastsSerializer(obj.broadcast).data
        return None 
