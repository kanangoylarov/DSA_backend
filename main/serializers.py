# from rest_framework import serializers
# from .models import Mətinlər, Müraciət, Əlaqə, Qeydiyyat, Sessiyalar, Nümayişlər, Sillabuslar, Təlimçilər,Məzunlar,Müəllimlər



# class ApplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Müraciət
#         fields = '__all__'
        
        
        
# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Əlaqə
#         fields = '__all__'
        
        
        
# class SubscribeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Qeydiyyat
#         fields = '__all__'



# class SessionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sessiyalar
#         fields = '__all__'

# class BroadcastsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Nümayişlər
#         fields = '__all__'

# class SyllabusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sillabuslar
#         fields = '__all__'
        
# class TrainerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Təlimçilər
#         fields = '__all__'

# class ScriptsSerializer(serializers.ModelSerializer):
#     sessions = SessionsSerializer(many=True, read_only=True)
#     broadcast = BroadcastsSerializer(read_only=True)
#     syllabus = SyllabusSerializer(many=True, read_only=True)
#     Trainer = TrainerSerializer(many=True, read_only=True)

#     class Meta:
#         model = Mətinlər
#         fields = '__all__'

#     def get_broadcast(self, obj):
#         if hasattr(obj, 'broadcast'):
#             return BroadcastsSerializer(obj.broadcast).data
#         return None 



# class TeachersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Müəllimlər
#         fields = '__all__'
        
        
# class GraduatesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Məzunlar
#         fields = '__all__'








from rest_framework import serializers
from .models import (
    Müraciət,
    Əlaqə,
    Qeydiyyat,
    Bootcamps,
    BootcampTipi,
    Təlimlər,
    Mətinlər,
    Sessiyalar,
    Nümayişlər,
    Sillabuslar,
    Təlimçilər,
    Müəllimlər,
    Məzunlar,
    FAQ
)


class MüraciətSerializer(serializers.ModelSerializer):
    class Meta:
        model = Müraciət
        fields = '__all__'


class ƏlaqəSerializer(serializers.ModelSerializer):
    class Meta:
        model = Əlaqə
        fields = '__all__'


class QeydiyyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qeydiyyat
        fields = '__all__'


class BootcampsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bootcamps
        fields = '__all__'


class BootcampTipiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootcampTipi
        fields = '__all__'


class TəlimlərSerializer(serializers.ModelSerializer):
    class Meta:
        model = Təlimlər
        fields = '__all__'


class MətinlərSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mətinlər
        fields = '__all__'


class SessiyalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessiyalar
        fields = '__all__'


class NümayişlərSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nümayişlər
        fields = '__all__'


class SillabuslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sillabuslar
        fields = '__all__'


class TəlimçilərSerializer(serializers.ModelSerializer):
    class Meta:
        model = Təlimçilər
        fields = '__all__'


class MüəllimlərSerializer(serializers.ModelSerializer):
    class Meta:
        model = Müəllimlər
        fields = '__all__'


class MəzunlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Məzunlar
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'