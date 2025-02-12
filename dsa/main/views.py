from django.shortcuts import render, redirect
from .forms import ApplyForm, ContactForm, SubscribeForm


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


