from django import forms
from .models import Apply, Contact, Subscribe

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
