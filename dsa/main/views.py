from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Apply, Contact, Subscribe
from .serializers import ApplySerializer, ContactSerializer, SubscribeSerializer
from django.http import JsonResponse

# Apply ViewSet
class ApplyViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

# Contact ViewSet
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Subscribe ViewSet
class SubscribeViewSet(viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

# Success Mesajı İçin API Endpoint
@api_view(['GET'])
def success_view(request):
    return Response({'message': 'Form başarıyla gönderildi!'})

@api_view(['GET'])
def apply_view(request):
    return Response({"message": "Apply API çalışıyor!"})


@api_view(['GET'])
def contacts_view(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)
