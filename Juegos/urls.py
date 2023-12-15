from django.urls import path

from Juegos.views import show_html, JuegoList, crear_juego_form, JuegoDetalle, JuegoBorrar, JuegoEditar

urlpatterns = [
    path('show/', show_html),
    path('list/', JuegoList.as_view(), name="JuegoLista"),
    path('crear/', crear_juego_form),
    path('juego/<int:pk>', JuegoDetalle.as_view(), name="JuegoDetalle"),
    path('editar/<int:pk>', JuegoEditar.as_view(), name="JuegoEditar"),
    path('eliminar/<int:pk>', JuegoBorrar.as_view(), name="JuegoBorrar"),

]