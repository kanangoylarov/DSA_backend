# from rest_framework import viewsets
# from .models import Mətinlər, Müraciət, Əlaqə, Qeydiyyat, Sessiyalar, Nümayişlər, Sillabuslar, Təlimçilər,Məzunlar,Müəllimlər
# from .serializers import ScriptsSerializer, SessionsSerializer, BroadcastsSerializer, SyllabusSerializer, TrainerSerializer, ApplySerializer, ContactSerializer, SubscribeSerializer, TeachersSerializer, GraduatesSerializer





# class ApplyViewSet(viewsets.ModelViewSet):
#     queryset = Müraciət.objects.all()
#     serializer_class = ApplySerializer
    
# class ContactViewSet(viewsets.ModelViewSet):
#     queryset = Əlaqə.objects.all()
#     serializer_class = ContactSerializer
    
    

# class SubscribeViewSet(viewsets.ModelViewSet):
#     queryset = Qeydiyyat.objects.all()
#     serializer_class = SubscribeSerializer

# # SESSIONS API
# class SessionsViewSet(viewsets.ModelViewSet):
#     queryset = Sessiyalar.objects.all()
#     serializer_class = SessionsSerializer

# # BROADCASTS API
# class BroadcastsViewSet(viewsets.ModelViewSet):
#     queryset = Nümayişlər.objects.all()
#     serializer_class = BroadcastsSerializer

# # SYLLABUS API
# class SyllabusViewSet(viewsets.ModelViewSet):
#     queryset = Sillabuslar.objects.all()
#     serializer_class = SyllabusSerializer
# # TRAINERS API  
# class TrainerViewSet(viewsets.ModelViewSet):
#     queryset = Təlimçilər.objects.all()
#     serializer_class = TrainerSerializer


# class ScriptsViewSet(viewsets.ModelViewSet):
#     queryset = Mətinlər.objects.prefetch_related('sessions', 'syllabus','trainers').select_related('broadcast')
#     serializer_class = ScriptsSerializer

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['request'] = self.request 
#         return context

# class TeachersViewSet(viewsets.ModelViewSet):
#     queryset = Müəllimlər.objects.all()
#     serializer_class = TeachersSerializer
    
# class GraduatesViewSet(viewsets.ModelViewSet):
#     queryset = Məzunlar.objects.all()
#     serializer_class = GraduatesSerializer








from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Müraciət, Əlaqə, Qeydiyyat, Bootcamps, BootcampTipi, Təlimlər, Mətinlər, Sessiyalar, Nümayişlər, Sillabuslar, Təlimçilər, Müəllimlər, Məzunlar


# Müraciət views
class MüraciətListView(ListView):
    model = Müraciət
    template_name = 'müraciət_list.html'


class MüraciətDetailView(DetailView):
    model = Müraciət
    template_name = 'müraciət_detail.html'


class MüraciətCreateView(CreateView):
    model = Müraciət
    fields = ['name', 'surname', 'email', 'phone']
    template_name = 'müraciət_form.html'
    success_url = reverse_lazy('müraciət_list')


class MüraciətUpdateView(UpdateView):
    model = Müraciət
    fields = ['name', 'surname', 'email', 'phone']
    template_name = 'müraciət_form.html'
    success_url = reverse_lazy('müraciət_list')


class MüraciətDeleteView(DeleteView):
    model = Müraciət
    template_name = 'müraciət_confirm_delete.html'
    success_url = reverse_lazy('müraciət_list')


# Əlaqə views
class ƏlaqəListView(ListView):
    model = Əlaqə
    template_name = 'əlaqə_list.html'


class ƏlaqəDetailView(DetailView):
    model = Əlaqə
    template_name = 'əlaqə_detail.html'


class ƏlaqəCreateView(CreateView):
    model = Əlaqə
    fields = ['name', 'surname', 'email', 'phone', 'message', 'category']
    template_name = 'əlaqə_form.html'
    success_url = reverse_lazy('əlaqə_list')


class ƏlaqəUpdateView(UpdateView):
    model = Əlaqə
    fields = ['name', 'surname', 'email', 'phone', 'message', 'category']
    template_name = 'əlaqə_form.html'
    success_url = reverse_lazy('əlaqə_list')


class ƏlaqəDeleteView(DeleteView):
    model = Əlaqə
    template_name = 'əlaqə_confirm_delete.html'
    success_url = reverse_lazy('əlaqə_list')


# Qeydiyyat views
class QeydiyyatListView(ListView):
    model = Qeydiyyat
    template_name = 'qeydiyyat_list.html'


class QeydiyyatDetailView(DetailView):
    model = Qeydiyyat
    template_name = 'qeydiyyat_detail.html'


class QeydiyyatCreateView(CreateView):
    model = Qeydiyyat
    fields = ['full_name', 'email', 'phone', 'event_date']
    template_name = 'qeydiyyat_form.html'
    success_url = reverse_lazy('qeydiyyat_list')


class QeydiyyatUpdateView(UpdateView):
    model = Qeydiyyat
    fields = ['full_name', 'email', 'phone', 'event_date']
    template_name = 'qeydiyyat_form.html'
    success_url = reverse_lazy('qeydiyyat_list')


class QeydiyyatDeleteView(DeleteView):
    model = Qeydiyyat
    template_name = 'qeydiyyat_confirm_delete.html'
    success_url = reverse_lazy('qeydiyyat_list')


# Bootcamps views
class BootcampsListView(ListView):
    model = Bootcamps
    template_name = 'bootcamps_list.html'


class BootcampsDetailView(DetailView):
    model = Bootcamps
    template_name = 'bootcamps_detail.html'


class BootcampsCreateView(CreateView):
    model = Bootcamps
    fields = ['name', 'order', 'is_active']
    template_name = 'bootcamps_form.html'
    success_url = reverse_lazy('bootcamps_list')


class BootcampsUpdateView(UpdateView):
    model = Bootcamps
    fields = ['name', 'order', 'is_active']
    template_name = 'bootcamps_form.html'
    success_url = reverse_lazy('bootcamps_list')


class BootcampsDeleteView(DeleteView):
    model = Bootcamps
    template_name = 'bootcamps_confirm_delete.html'
    success_url = reverse_lazy('bootcamps_list')


# BootcampTipi views
class BootcampTipiListView(ListView):
    model = BootcampTipi
    template_name = 'bootcamptipi_list.html'


class BootcampTipiDetailView(DetailView):
    model = BootcampTipi
    template_name = 'bootcamptipi_detail.html'


class BootcampTipiCreateView(CreateView):
    model = BootcampTipi
    fields = ['bootcamp', 'name', 'order', 'is_active']
    template_name = 'bootcamptipi_form.html'
    success_url = reverse_lazy('bootcamptipi_list')


class BootcampTipiUpdateView(UpdateView):
    model = BootcampTipi
    fields = ['bootcamp', 'name', 'order', 'is_active']
    template_name = 'bootcamptipi_form.html'
    success_url = reverse_lazy('bootcamptipi_list')


class BootcampTipiDeleteView(DeleteView):
    model = BootcampTipi
    template_name = 'bootcamptipi_confirm_delete.html'
    success_url = reverse_lazy('bootcamptipi_list')


# Təlimlər views
class TəlimlərListView(ListView):
    model = Təlimlər
    template_name = 'təlimlər_list.html'


class TəlimlərDetailView(DetailView):
    model = Təlimlər
    template_name = 'təlimlər_detail.html'


class TəlimlərCreateView(CreateView):
    model = Təlimlər
    fields = ['bootcamp_type', 'is_active', 'order', 'title']
    template_name = 'təlimlər_form.html'
    success_url = reverse_lazy('təlimlər_list')


class TəlimlərUpdateView(UpdateView):
    model = Təlimlər
    fields = ['bootcamp_type', 'is_active', 'order', 'title']
    template_name = 'təlimlər_form.html'
    success_url = reverse_lazy('təlimlər_list')


class TəlimlərDeleteView(DeleteView):
    model = Təlimlər
    template_name = 'təlimlər_confirm_delete.html'
    success_url = reverse_lazy('təlimlər_list')


# Mətinlər views
class MətinlərListView(ListView):
    model = Mətinlər
    template_name = 'mətinlər_list.html'


class MətinlərDetailView(DetailView):
    model = Mətinlər
    template_name = 'mətinlər_detail.html'


class MətinlərCreateView(CreateView):
    model = Mətinlər
    fields = ['trainings', 'title', 'description', 'information', 'money', 'image', 'for_who', 'certificates', 'certificate_image']
    template_name = 'mətinlər_form.html'
    success_url = reverse_lazy('mətinlər_list')


class MətinlərUpdateView(UpdateView):
    model = Mətinlər
    fields = ['trainings', 'title', 'description', 'information', 'money', 'image', 'for_who', 'certificates', 'certificate_image']
    template_name = 'mətinlər_form.html'
    success_url = reverse_lazy('mətinlər_list')


class MətinlərDeleteView(DeleteView):
    model = Mətinlər
    template_name = 'mətinlər_confirm_delete.html'
    success_url = reverse_lazy('mətinlər_list')


# Sessiyalar views
class SessiyalarListView(ListView):
    model = Sessiyalar
    template_name = 'sessiyalar_list.html'


class SessiyalarDetailView(DetailView):
    model = Sessiyalar
    template_name = 'sessiyalar_detail.html'


class SessiyalarCreateView(CreateView):
    model = Sessiyalar
    fields = ['script', 'session_number', 'date', 'hour']
    template_name = 'sessiyalar_form.html'
    success_url = reverse_lazy('sessiyalar_list')


class SessiyalarUpdateView(UpdateView):
    model = Sessiyalar
    fields = ['script', 'session_number', 'date', 'hour']
    template_name = 'sessiyalar_form.html'
    success_url = reverse_lazy('sessiyalar_list')


class SessiyalarDeleteView(DeleteView):
    model = Sessiyalar
    template_name = 'sessiyalar_confirm_delete.html'
    success_url = reverse_lazy('sessiyalar_list')


# Nümayişlər views
class NümayişlərListView(ListView):
    model = Nümayişlər
    template_name = 'nümayişlər_list.html'


class NümayişlərDetailView(DetailView):
    model = Nümayişlər
    template_name = 'nümayişlər_detail.html'


class NümayişlərCreateView(CreateView):
    model = Nümayişlər
    fields = ['script', 'title', 'info', 'link', 'trainer']
    template_name = 'nümayişlər_form.html'
    success_url = reverse_lazy('nümayişlər_list')


class NümayişlərUpdateView(UpdateView):
    model = Nümayişlər
    fields = ['script', 'title', 'info', 'link', 'trainer']
    template_name = 'nümayişlər_form.html'
    success_url = reverse_lazy('nümayişlər_list')


class NümayişlərDeleteView(DeleteView):
    model = Nümayişlər
    template_name = 'nümayişlər_confirm_delete.html'
    success_url = reverse_lazy('nümayişlər_list')


# Sillabuslar views
class SillabuslarListView(ListView):
    model = Sillabuslar
    template_name = 'sillabuslar_list.html'


class SillabuslarDetailView(DetailView):
    model = Sillabuslar
    template_name = 'sillabuslar_detail.html'


class SillabuslarCreateView(CreateView):
    model = Sillabuslar
    fields = ['script', 'title', 'description', 'label', 'information']
    template_name = 'sillabuslar_form.html'
    success_url = reverse_lazy('sillabuslar_list')


class SillabuslarUpdateView(UpdateView):
    model = Sillabuslar
    fields = ['script', 'title', 'description', 'label', 'information']
    template_name = 'sillabuslar_form.html'
    success_url = reverse_lazy('sillabuslar_list')


class SillabuslarDeleteView(DeleteView):
    model = Sillabuslar
    template_name = 'sillabuslar_confirm_delete.html'
    success_url = reverse_lazy('sillabuslar_list')


# Təlimçilər views
class TəlimçilərListView(ListView):
    model = Təlimçilər
    template_name = 'təlimçilər_list.html'


class TəlimçilərDetailView(DetailView):
    model = Təlimçilər
    template_name = 'təlimçilər_detail.html'


class TəlimçilərCreateView(CreateView):
    model = Təlimçilər
    fields = ['script', 'info', 'name', 'work_location', 'image']
    template_name = 'təlimçilər_form.html'
    success_url = reverse_lazy('təlimçilər_list')


class TəlimçilərUpdateView(UpdateView):
    model = Təlimçilər
    fields = ['script', 'info', 'name', 'work_location', 'image']
    template_name = 'təlimçilər_form.html'
    success_url = reverse_lazy('təlimçilər_list')


class TəlimçilərDeleteView(DeleteView):
    model = Təlimçilər
    template_name = 'təlimçilər_confirm_delete.html'
    success_url = reverse_lazy('təlimçilər_list')


# Müəllimlər views
class MüəllimlərListView(ListView):
    model = Müəllimlər
    template_name = 'müəllimlər_list.html'


class MüəllimlərDetailView(DetailView):
    model = Müəllimlər
    template_name = 'müəllimlər_detail.html'


class MüəllimlərCreateView(CreateView):
    model = Müəllimlər
    fields = ['info', 'name', 'work_position', 'work_location', 'image']
    template_name = 'müəllimlər_form.html'
    success_url = reverse_lazy('müəllimlər_list')


class MüəllimlərUpdateView(UpdateView):
    model = Müəllimlər
    fields = ['info', 'name', 'work_position', 'work_location', 'image']
    template_name = 'müəllimlər_form.html'
    success_url = reverse_lazy('müəllimlər_list')


class MüəllimlərDeleteView(DeleteView):
    model = Müəllimlər
    template_name = 'müəllimlər_confirm_delete.html'
    success_url = reverse_lazy('müəllimlər_list')


# Məzunlar views
class MəzunlarListView(ListView):
    model = Məzunlar
    template_name = 'məzunlar_list.html'


class MəzunlarDetailView(DetailView):
    model = Məzunlar
    template_name = 'məzunlar_detail.html'


class MəzunlarCreateView(CreateView):
    model = Məzunlar
    fields = ['name', 'work_position', 'work_location', 'image']
    template_name = 'məzunlar_form.html'
    success_url = reverse_lazy('məzunlar_list')


class MəzunlarUpdateView(UpdateView):
    model = Məzunlar
    fields = ['name', 'work_position', 'work_location', 'image']
    template_name = 'məzunlar_form.html'
    success_url = reverse_lazy('məzunlar_list')


class MəzunlarDeleteView(DeleteView):
    model = Məzunlar
    template_name = 'məzunlar_confirm_delete.html'
    success_url = reverse_lazy('məzunlar_list')
