from django import forms
from .models import FormNames, AppointmentSection, SubscribeForm


class ModelFormNames(forms.ModelForm):
    class Meta:
        model = FormNames
        fields = '__all__'


class AppointmentSectionFormNames(forms.ModelForm):
    class Meta:
        model = AppointmentSection
        fields = '__all__'


class ModalSubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeForm
        fields = '__all__'

