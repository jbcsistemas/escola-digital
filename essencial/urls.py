from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import FormEntrar
from .views import home

app_name = 'essencial'
urlpatterns = [
    path('', home),
    path('entrar/',
         auth_views.LoginView.as_view(
             authentication_form=FormEntrar),
         name='entrar',
         ),
    path('sair/',
         auth_views.LogoutView.as_view(),
         name='sair',
         ),
]
