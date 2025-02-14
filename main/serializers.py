from rest_framework import serializers
from .models import Scripts, Sessions, Broadcasts, Syllabus, Trainer,Apply, Contact, Subscribe



class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'
        
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
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
        
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class ScriptsSerializer(serializers.ModelSerializer):
    sessions = SessionsSerializer(many=True, read_only=True)
    broadcast = BroadcastsSerializer(read_only=True)
    syllabus = SyllabusSerializer(many=True, read_only=True)
    Trainer = TrainerSerializer(many=True, read_only=True)

    class Meta:
        model = Scripts
        fields = '__all__'

    def get_broadcast(self, obj):
        if hasattr(obj, 'broadcast'):
            return BroadcastsSerializer(obj.broadcast).data
        return None 
