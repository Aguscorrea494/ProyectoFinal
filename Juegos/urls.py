from django.urls import path

from Juegos.views import show_html, JuegoDetalle, JuegoBorrar, JuegoEditar, \
    busqueda_juego, detalle_creador, JuegoList, CrearJuego, comentarios

urlpatterns = [
    path('show/', show_html, name="Inicio"),
    path('list/', JuegoList.as_view(), name="JuegoLista"),
    path('crear/',CrearJuego.as_view()),
    path('juego/<int:pk>', JuegoDetalle.as_view(), name="JuegoDetalle"),
    path('editar/<int:pk>', JuegoEditar.as_view(), name="JuegoEditar"),
    path('eliminar/<int:pk>', JuegoBorrar.as_view(), name="JuegoBorrar"),
    path('acerca_de_mi/', detalle_creador),
    path('busca/', busqueda_juego),
    path('comentario/', comentarios)



]