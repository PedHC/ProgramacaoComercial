from django.contrib import admin
from veiculos.models import *

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['marca','modelo','ano_fabricacao','modelo_fabricacao','combustivel']
    search_fields = ['marca','modelo']
    list_filter = ['combustivel']

admin.site.register(Veiculo, VeiculoAdmin)
# Register your models here.
