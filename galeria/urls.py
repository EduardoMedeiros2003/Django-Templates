# Aqui vai todas as rotas de galeria deste app
from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index)
]