from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import IndexView, LoginView, ReceitaView, CadastroReceitaView, ListaReceitasView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth', include('social_django.urls', namespace='social')),
    #path('<int:pk>', ReceitaView.as_view(), name='login'),
    path('cadastro-receita', CadastroReceitaView.as_view(), name='cadastro-receita'),
]