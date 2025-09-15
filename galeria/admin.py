from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome","publicada", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ["nome"] #el campo necesita ser una tupla o list ("nome" ,) tambien sirve
    list_filter = ("categoria", )
    list_editable = ("publicada", )
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
