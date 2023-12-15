from django import forms
from datetime import datetime


class BlogForm(forms.Form):
    nombre = forms.CharField()
    plataforma = forms.CharField()
    descripcion = forms.CharField()
    autor = forms.CharField()
    # imagen = forms.ImageField()


