from django.db import models

class Osso(models.Model):
    
    nome = models.CharField(max_length=100)
    objeto3D = models.FileField(upload_to="modelo3D/", blank=True, null=True)
    descricao = models.CharField(max_length=1000,null=True);

    def __str__(self):
        return self.nome