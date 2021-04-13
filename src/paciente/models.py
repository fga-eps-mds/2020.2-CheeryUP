from django.db import models
from users.models import Psicologo


# Create your models here.
class Paciente(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('P', 'Prefiro não responder'),
    )
    REGIAO = (
        ('AC', 'Águas Claras'),
        ('AS', 'Asa Sul'),
        ('AN', 'Asa Norte'),
        ('CI', 'Ceilândia'),
        ('GA', 'Gama'),
        ('GA', 'Guará'),
        ('RE', 'Recanto das Emas'),
        ('RF', 'Riacho Fundo'),
        ('SA', 'Samambaia'),
        ('SO', 'Sobradinho'),
        ('TA', 'Taguatinga'),
        ('EO', 'Entre outros'),
    )
    SITUACAO = (
        ('C', 'Controlada'),
        ('M', 'Moderada'),
        ('G', 'Grave'),
    )
    nome = models.CharField('Nome completo',max_length=90)
    data_nascimento = models.DateField()
    psicologo = models.ForeignKey(Psicologo, null=False, on_delete=models.CASCADE)
    genero = models.CharField(default = True, max_length=1, choices=GENERO)
    regiao = models.CharField(max_length=3, choices=REGIAO)
    situacao = models.CharField(default = True,blank=False, max_length=2, choices=SITUACAO)
    descricao = models.TextField(blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, default=False)

    
    def __str__(self):
        return self.nome
        
