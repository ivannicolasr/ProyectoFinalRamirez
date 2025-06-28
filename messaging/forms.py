from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=User.objects.all(), label='Para')

    class Meta:
        model = Mensaje
        fields = ['receptor', 'asunto', 'contenido']