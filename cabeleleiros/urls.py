from django.urls import path
from cabeleleiros import views

urlpatterns = [
    path('', views.HorarioList.as_view(), name = "lista_horario"),
    path('novo/', views.HorarioNew.as_view(), name = "novo_horario"),
    path('cliente/novo/', views.ClientesNew.as_view(), name = "novo_cliente"),
    path('cliente/<int:pk>/', views.ClienteEdit.as_view(), name = "editar_cliente"),
    path('cliente/', views.ClientesList.as_view(), name = "lista_clientes"),
    path('cliente/excluir/<int:pk>/', views.ClienteDelete.as_view(), name = "excluir_cliente"),
    path('<int:pk>/', views.HorarioEdit.as_view(), name = "editar_horario"),
    path('excluir/<int:pk>/', views.HorarioDelete.as_view(), name = "cancelar_horario"),
    path('api/listar/', views.HorarioListAPI.as_view(), name = "api_listar_horarios"),
]