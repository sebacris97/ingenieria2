"""bookflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookflixapp import views
from django.conf.urls import url, include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index),
    path('verLibros/',views.ver_libros),
    
    path('verCapitulos/<int:pk>',views.ver_capitulos),
    #<int:pk> significa que ver capitulos recibe de parametro la en pk
    #la clave primaria del libro desde el template que se lo llama (desde verLibros)

    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),

    #path('accounts/', include('django.contrib.auth.urls')),

    #path('agregarLibro/',views.agregar_libro),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
