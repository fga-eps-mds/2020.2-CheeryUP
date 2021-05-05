from django.db import models
from django.contrib.auth.models import User


class Psicologo(models.Model):
    GENERO = (
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('P', 'Prefiro não responder'),
        )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True)
    nCRP = models.CharField(max_length=11, unique=True)
    bio = models.TextField()
    genero = models.CharField(default='P', max_length=1, choices=GENERO)
    name = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.user.username
