from django.urls import path
from veiculos import views

urlpatterns = [
    path('', views.VeiculosList.as_view(), name = "lista_veiculos"),
    path('novo/', views.VeiculosNew.as_view(), name = "novo_veiculo"),
]