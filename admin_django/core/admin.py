from django.contrib import admin
from .models import Categoria, Produto

#admin.site.register(Produto)
#admin.site.register(Categoria)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','preco','categoria')
    list_filter = ('categoria',) # em python uma tupla só com um elemento tem que ter a vírgula
    list_editable = ('preco','categoria')
    list_display_links = ('nome','descricao')
    search_fields = ('nome','descricao')

# Register your models here.
