from django import forms

class BlogForm(forms.Form):
    nombre = forms.CharField()
    subnombre = forms.CharField()
    cuerpo = forms.CharField()
    autor = forms.CharField()
    # fecha = forms.IntegerField()

    # imagen = forms.ImageField()


