from django.contrib import admin
from .models import Libro, Genero, Autor, Editorial, Novedad, Capitulo
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


# Register your models here.


# esto es una clase que pone el formulario de Capitulo en una linea
class CapituloInline(admin.TabularInline):
    model = Capitulo


# esto se llama decorator y ahorra el trabajo de registrar la clase y el libro
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):

    def get_genero(self, obj):
        return ", ".join([p.nombre for p in obj.genero.all()])

    get_genero.admin_order_field = 'genero'  # Allows column order sorting
    get_genero.short_description = 'genero'  # Renames column head

    filter_horizontal = ('genero',)
    list_display = ('titulo', 'nropaginas', 'nrocapitulos', 'isbn', 'autor', 'editorial', 'get_genero', 'agnoedicion',)
    search_fields = ('titulo', 'autor__nombre', 'editorial__nombre', 'genero__nombre',)
    list_filter = ('autor', 'editorial', ('agnoedicion', DateRangeFilter), 'genero')
    inlines = [CapituloInline]  # se registra en liro la clase creada anteriormente


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'creacion',)
    search_fields = ('titulo', 'texto',)
    list_filter = (('creacion', DateTimeRangeFilter), 'creacion')


admin.site.site_header = 'Sitio de administracion de Bookflix'
admin.site.index_title = 'Sitio de administracion de Bookflix'
admin.site.index_title = "Bienvenido al panel de administracion de Bookflix"
