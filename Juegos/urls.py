from django.urls import path

from Juegos.views import show_html, JuegoList, JuegoCreate, crear_juego_form

urlpatterns = [
    path('show/', show_html),
    path('list/', JuegoList.as_view()),
    path('crear/', crear_juego_form)

]