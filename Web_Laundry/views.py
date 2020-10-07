from django.shortcuts import render, redirect
from .forms import ModelFormNames, AppointmentSectionFormNames, ModalSubscribeForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = AppointmentSectionFormNames(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your form was submitted successfully')
            return redirect('index')
        else:
            messages.info(request, 'form was not submitted, there was an error try again ')

            return render(request, 'index.html', {})
    return render(request, 'index.html', {})


def contact_page(request):
    if request.method == 'POST':
        form = ModelFormNames(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(request, 'Mr ' + username + '' + ' For Contacting Us.. We will Get Back To You')
            return render(request, 'contact.html', {})
        form3 = ModalSubscribeForm(request.POST)
        if form3.is_valid():
            form3.save()
            messages.info(request, 'Your Email is Save...we Shall Keep You Ubdate With Latest Content About Our Site')
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'services.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def blog(request):
    return render(request, 'blog.html', {})


