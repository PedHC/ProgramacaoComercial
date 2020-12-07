from django.urls import path
from veiculos import views

urlpatterns = [
    path('', views.VeiculosList.as_view(), name = "lista_veiculos"),
    path('novo/', views.VeiculosNew.as_view(), name = "novo_veiculo"),
    path('<int:pk>/', views.VeiculosEdit.as_view(), name = "editar_veiculo"),
    path('excluir/<int:pk>/', views.VeiculosDelete.as_view(), name = "deletar_veiculo"),
    path('api/listar/', views.VeiculosListAPI.as_view(), name = "api_listar_veiculo"),
]