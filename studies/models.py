from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Materia(models.Model):
    """Model definition for Materia."""

    # TODO: Define fields here
    user = models.ForeignKey(User, verbose_name="usuário", on_delete=models.CASCADE)
    nome = models.CharField("nome", max_length=100)
    descricao = models.TextField("descricao")
    cor = models.CharField("cor", max_length=7) # Receber hex
    created_at = models.DateField('Criado em', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        """Meta definition for Materia."""

        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        """Unicode representation of Materia."""
        return self.nome