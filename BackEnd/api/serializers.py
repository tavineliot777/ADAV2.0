from rest_framework import serializers
from .models import Osso

class OssoSerializer(serializers.ModelSerializer):
   class Meta:
    model = Osso
    fields = ["nome", "objeto3D","descricao"]
