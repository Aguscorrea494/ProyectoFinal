from django import forms
from datetime import datetime

from Juegos.models import Comentarios, Juegos


class BlogForm(forms.ModelForm):

    class Meta:
        model = Juegos
        fields = "__all__"
class BusquedadForm(forms.Form):
    nombre = forms.CharField()

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = "__all__"



