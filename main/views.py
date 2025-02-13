from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ApplyForm, ContactForm, SubscribeForm,Scripts, Sessions, Broadcasts, Syllabus


def apply_view(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplyForm()
    
    return render(request, 'apply_form.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SubscribeForm()

    return render(request, 'subscribe_form.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')


##New Views for Scripts--------------------------------------------------------------------------------------------------
class ScriptsListView(ListView):
    model = Scripts
    template_name = 'scripts/scripts_list.html'
    context_object_name = 'scripts'

class ScriptsDetailView(DetailView):
    model = Scripts
    template_name = 'scripts/scripts_detail.html'
    context_object_name = 'script'

class ScriptsCreateView(CreateView):
    model = Scripts
    template_name = 'scripts/scripts_form.html'
    fields = ['title', 'description', 'information', 'image', 'for_who', 'certificates', 'certificate_image']

class ScriptsUpdateView(UpdateView):
    model = Scripts
    template_name = 'scripts/scripts_form.html'
    fields = ['title', 'description', 'information', 'image', 'for_who', 'certificates', 'certificate_image']

class ScriptsDeleteView(DeleteView):
    model = Scripts
    template_name = 'scripts/scripts_confirm_delete.html'
    success_url = reverse_lazy('scripts_list')




class SessionsListView(ListView):
    model = Sessions
    template_name = 'sessions/sessions_list.html'
    context_object_name = 'sessions'

class SessionsDetailView(DetailView):
    model = Sessions
    template_name = 'sessions/sessions_detail.html'
    context_object_name = 'session'

class SessionsCreateView(CreateView):
    model = Sessions
    template_name = 'sessions/sessions_form.html'
    fields = ['session_number', 'date', 'hour']

class SessionsUpdateView(UpdateView):
    model = Sessions
    template_name = 'sessions/sessions_form.html'
    fields = ['session_number', 'date', 'hour']

class SessionsDeleteView(DeleteView):
    model = Sessions
    template_name = 'sessions/sessions_confirm_delete.html'
    success_url = reverse_lazy('sessions_list')




class BroadcastsListView(ListView):
    model = Broadcasts
    template_name = 'broadcasts/broadcasts_list.html'
    context_object_name = 'broadcasts'

class BroadcastsDetailView(DetailView):
    model = Broadcasts
    template_name = 'broadcasts/broadcasts_detail.html'
    context_object_name = 'broadcast'

class BroadcastsCreateView(CreateView):
    model = Broadcasts
    template_name = 'broadcasts/broadcasts_form.html'
    fields = ['title', 'info', 'link', 'trainer']

class BroadcastsUpdateView(UpdateView):
    model = Broadcasts
    template_name = 'broadcasts/broadcasts_form.html'
    fields = ['title', 'info', 'link', 'trainer']

class BroadcastsDeleteView(DeleteView):
    model = Broadcasts
    template_name = 'broadcasts/broadcasts_confirm_delete.html'
    success_url = reverse_lazy('broadcasts_list')


class SyllabusListView(ListView):
    model = Syllabus
    template_name = 'syllabus/syllabus_list.html'
    context_object_name = 'syllabus_list'

class SyllabusDetailView(DetailView):
    model = Syllabus
    template_name = 'syllabus/syllabus_detail.html'
    context_object_name = 'syllabus_item'

class SyllabusCreateView(CreateView):
    model = Syllabus
    template_name = 'syllabus/syllabus_form.html'
    fields = ['title', 'description','label' ,'information']

class SyllabusUpdateView(UpdateView):
    model = Syllabus
    template_name = 'syllabus/syllabus_form.html'
    fields = ['title', 'description','label', 'information']

class SyllabusDeleteView(DeleteView):
    model = Syllabus
    template_name = 'syllabus/syllabus_confirm_delete.html'
    success_url = reverse_lazy('syllabus_list')




