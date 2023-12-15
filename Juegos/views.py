from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from Juegos.forms import BlogForm
from Juegos.models import Juegos


def show_html(request):
    juego = Juegos.objects.all()
    contexto = {
        "juego" : juego
    }
    return render(request, template_name= "Templates/base.html", context= contexto)

class JuegoList(ListView):
    model = Juegos
    template_name = "Blogs/blogs.html"

def crear_juego_form(request):
    if request.method == "POST":
        blog_formulario = BlogForm(request.POST)
        if blog_formulario.is_valid():
            informacion = blog_formulario.cleaned_data
            juego_agregar = Juegos(nombre=informacion["nombre"], subnombre=informacion["subnombre"], cuerpo=informacion["cuerpo"], autor=informacion["autor"], )
            juego_agregar.save()
            return redirect("/apps/list/")

    form = BlogForm()
    contexto = {
        "form": form
    }
    return render(request, template_name="Blogs/formulario_crear.html", context=contexto)
class JuegoDetalle(DetailView):
    model =  Juegos
    template_name = "Blogs/juego_detalle.html"

class JuegoEditar(UpdateView):
    model = Juegos
    success_url = "/apps/list/"
    template_name = ("Blogs/formulario_crear.html")
    fields = ["nombre","subnombre","cuerpo"]

class JuegoBorrar(DeleteView):
    model = Juegos
    success_url = "/apps/list/"
    template_name = "Blogs/eliminar_juego.html"

