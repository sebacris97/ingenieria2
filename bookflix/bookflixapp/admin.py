from django.contrib import admin
from .models import Libro, Genero, Autor, Editorial, Novedad
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.


class LibroAdmin(admin.ModelAdmin):

    def get_genero(self,obj):
        return ", ".join([p.nombre for p in obj.genero.all()])
    
    get_genero.admin_order_field  = 'genero'  #Allows column order sorting
    get_genero.short_description = 'genero'  #Renames column head    

    filter_horizontal = ('genero',)
    list_display=('titulo','nropaginas','nrocapitulos','isbn','autor','editorial','get_genero','agnoedicion',)
    search_fields=('titulo','autor__nombre','editorial__nombre','genero__nombre',)
    list_filter=('autor','editorial', ('agnoedicion', DateRangeFilter),'genero')




class GeneroAdmin(admin.ModelAdmin):

    list_display=('nombre',)
    search_fields=('nombre',)


class AutorAdmin(admin.ModelAdmin):

    list_display=('nombre','apellido')
    search_fields=('nombre','apellido')

class EditorialAdmin(admin.ModelAdmin):

    list_display=('nombre',)
    search_fields=('nombre',)


class NovedadAdmin(admin.ModelAdmin):

    list_display=('titulo','creada',)
    search_fields=('titulo','texto',)
    list_filter=(('creada', DateRangeFilter),)



admin.site.register(Libro,LibroAdmin)
admin.site.register(Genero,GeneroAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Editorial,EditorialAdmin)
admin.site.register(Novedad,NovedadAdmin)


admin.site.site_header='Sitio de administracion de Bookflix'
admin.site.index_title='Sitio de administracion de Bookflix'
admin.site.index_title = "Bienvenido al panel de administracion de Bookflix"

