from django.db import models

#Sempre que adicionar um novo model, tem que usar o comando 'python manage.py makemigrations' e depois o comando 'python manage.py migrate'

class Fotografia(models.Model):
    #Lista cheia de tuplas para o categoria = models.CharField pegar as informações 
    OPCOES_CATEGORIA = [
        ('NEBULOSA','Nebulosa'),
        ('ESTRELA','Estrela'),
        ('GALÁXIA','Galáxia'),
        ('PLANETA','Planeta')
    ]


    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA ,default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"