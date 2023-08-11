"""
URL configuration for pacyfic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from principal.views import *
from principal.views1 import *
from principal.views2 import *
from principal.views3 import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('principal/', include(('principal.urls','principal'))),
    path('principal1/', include(('principal.urls1','principal1'))),
    path('principal2/', include(('principal.urls2','principal2'))),
    path('principal3/', include(('principal.urls3','principal3'))),
    path('Home/', Home, name= 'index'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    path('parametro/', Parametros, name= 'indexparametro'),
    path('registro', SignUpView.as_view(template_name='register.html'), name='registro'),
    path('perfil/', Perfil, name= 'perfil'),
    path('general/', Parametros1, name= 'general'),
    path('cronograma/', Parametros2, name= 'cronograma'),
    path('programa/', Parametros3, name= 'programa'),
    path('catalogo/', Catalogo, name= 'catalogo'),
    path('', Home1, name= 'index1'),
    path('quienessomos/', quienessomos, name= 'quienessomos'),
    path('contacto/', contacto, name= 'contacto'),
 ]
