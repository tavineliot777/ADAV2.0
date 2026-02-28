from django.db import models
from django.core.validators import RegexValidator
class Osso(models.Model):
    
    nome = models.CharField(max_length=100,
               validators=[ RegexValidator(
                   regex= r'^[^0-9]*$',
                   message="O nome do Osso não pode conter números",
                   code="nome_invalido"
               )]
               )
    objeto3D = models.FileField(upload_to="modelo3D/", blank=True, null=True)
    descricao = models.TextField(null=True, blank=True);

    def __str__(self):
        return self.nome