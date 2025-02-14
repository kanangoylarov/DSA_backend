from django import forms
from .models import Apply, Contact, Subscribe, Scripts, Sessions, Broadcasts, Syllabus

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'surname', 'email', 'phone']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'phone', 'message', 'category']
        widgets = {
            'category': forms.Select(choices=Contact.CATEGORY_CHOICES),
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['full_name', 'email', 'phone', 'event_date']
        widgets = {
            'event_date': forms.SelectDateWidget,  # Takvim seçeneği
        }



##New Form for Scripts--------------------------------------------------------------------------------------------------



# Scripts Formu
class ScriptsForm(forms.ModelForm):
    class Meta:
        model = Scripts
        fields = ['title', 'description', 'information', 'image','money' 'for_who', 'certificates', 'certificate_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control'}),
            'for_who': forms.Textarea(attrs={'class': 'form-control'}),
            'certificates': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Sessions Formu
class SessionsForm(forms.ModelForm):
    class Meta:
        model = Sessions
        fields = ['session_number', 'date', 'hour']
        widgets = {
            'session_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hour': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

# Broadcasts Formu
class BroadcastsForm(forms.ModelForm):
    class Meta:
        model = Broadcasts
        fields = ['title', 'info', 'link', 'trainer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'trainer': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Syllabus Formu
class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['title', 'description','label', 'information']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control'}),
        }
