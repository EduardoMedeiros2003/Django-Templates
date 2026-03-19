# Aqui vai todas as rotas de galeria deste app
from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name= 'index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
]