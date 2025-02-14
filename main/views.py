from rest_framework import viewsets
from .models import Scripts, Sessions, Broadcasts, Syllabus, Trainer
from .serializers import ScriptsSerializer, SessionsSerializer, BroadcastsSerializer, SyllabusSerializer, TrainerSerializer

# SESSIONS API
class SessionsViewSet(viewsets.ModelViewSet):
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer

# BROADCASTS API
class BroadcastsViewSet(viewsets.ModelViewSet):
    queryset = Broadcasts.objects.all()
    serializer_class = BroadcastsSerializer

# SYLLABUS API
class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
# TRAINERS API  
class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class ScriptsViewSet(viewsets.ModelViewSet):
    queryset = Scripts.objects.prefetch_related('sessions', 'syllabus','trainers').select_related('broadcast')
    serializer_class = ScriptsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request 
        return context

