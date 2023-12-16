from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from Juegos.forms import BlogForm, BusquedadForm, ComentarioForm
from Juegos.models import Juegos, Comentarios


def show_html(request):
    juego = Juegos.objects.all()
    contexto = {
        "juego" : juego
    }
    return render(request, template_name= "Templates/base.html", context= contexto)

class JuegoList(ListView):
    model = Juegos
    template_name = "Blogs/blogs.html"

class CrearJuego(LoginRequiredMixin, CreateView):
    model = Juegos
    template_name = "Blogs/formulario_crear.html"
    success_url = "/apps/list/"
    fields = "__all__"
class JuegoDetalle(DetailView):
    model = Juegos
    template_name = "Blogs/juego_detalle.html"

class JuegoEditar(LoginRequiredMixin, UpdateView):
    model = Juegos
    success_url = "/apps/list/"
    template_name = ("Blogs/formulario_crear.html")
    fields = ["nombre","plataforma","descripcion"]


class JuegoBorrar(LoginRequiredMixin, DeleteView):
    model = Juegos
    success_url = "/apps/list/"
    template_name = "Blogs/eliminar_juego.html"

def detalle_creador(request):
    juego = Juegos.objects.all()
    contexto = {
        "juego": juego
    }
    return render(request, template_name="Blogs/credor_detalle.html", context=contexto)





def busqueda_juego(request):
   nombre = request.GET["nombre"]
   juegos = Juegos.objects.filter(nombre__icontains=nombre)
   contexto = {

       "juegos": juegos,
       "form": BusquedaForm()
   }
   return render(request, template_name="Blogs/blogs.html", context=contexto)


def comentarios(request):

    formulario = ComentarioForm(request.POST)
    if formulario.is_valid():
      informacion =  formulario.cleaned_data
      juego = Juegos.objects.get(id= informacion["juego"])
      comentario_crear = Comentarios(usuario=request.user, juego=juego, comentario=informacion["comentario"])
      comentario_crear.save()
      redirect("/apps/list/")






