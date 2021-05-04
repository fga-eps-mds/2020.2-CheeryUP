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
        ('AR', 'Arniqueira'), 
        ('BZ', 'Brazilandia'),
        ('CA', 'Candangolândia'), 
        ('CI', 'Ceilândia'),
        ('CZ', 'Cruzeiro'), 
        ('FE', 'Fercal'), 
        ('GA', 'Gama'),
        ('GR', 'Guará'),
        ('IT', 'Itapoã'), 
        ('JB', 'Jardim Botânico'),
        ('LS', 'Lago Sul'), 
        ('LN', 'Lago Norte'), 
        ('NB', 'Núcleo Bandeirante'),
        ('PW', 'Park Way'),
        ('PA', 'Paranoá'),
        ('PL', 'Planaltina'),
        ('PP', 'Plano Piloto'),
        ('RE', 'Recanto das Emas'),
        ('RF', 'Riacho Fundo'),
        ('SA', 'Samambaia'),
        ('SM', 'Santa Maria'),
        ('SB', 'São Sabastião'), 
        ('SCIA', 'SCIA'), 
        ('RF', 'Riacho Fundo'),
        ('RFII', 'Riacho Fundo II'), 
        ('SI', 'SIA'),
        ('SO', 'Sobradinho'),
        ('SOII', 'Sobradinho II'), 
        ('SN', 'Sol Nascente'), 
        ('SD', 'Sudoeste'),
        ('TA', 'Taguatinga'),
        ('VA',  'Varjão'), 
        ('VP', 'Vicente Pires'),
        ('EO', 'Entre outros'),
    )
    SITUACAO = (
        ('C', 'Controlada'),
        ('M', 'Moderada'),
        ('G', 'Grave'),
    )
    nome = models.CharField('Nome completo', max_length=90)
    data_nascimento = models.DateField()
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    genero = models.CharField(default=True, max_length=1, choices=GENERO)
    regiao = models.CharField(max_length=4, choices=REGIAO)
    situacao = models.CharField(default=True, blank=False, max_length=2, choices=SITUACAO)
    descricao = models.TextField(blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, default=False)

    def __str__(self):
        return self.nome
        
class Consulta(models.Model):
    SITUAÇAO = (
        (-1, 'Pior que antes'),
        (0, 'Sem mudança'),
        (1, 'Melhor que antes')
    )
  
    id = models.BigAutoField(primary_key=True)
    registro = models.CharField(unique=True, max_length=5, default=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    problemasPessoais = models.IntegerField(choices=SITUAÇAO, default=True)
    humor = models.IntegerField(choices=SITUAÇAO, default=False)
    estabilidadeDeEmoções = models.IntegerField(choices=SITUAÇAO, default=False)
    interessePelaVida = models.IntegerField(choices=SITUAÇAO, default=False)
    capacidadeDeSituaçõesDificeis = models.IntegerField(choices=SITUAÇAO, default=False)
    convivioFamiliar = models.IntegerField(choices=SITUAÇAO, default=False)
    energiaSono = models.IntegerField(choices=SITUAÇAO, default=False)
    convivioAmigos = models.IntegerField(choices=SITUAÇAO, default=False)
    conhecimentoDoenca = models.IntegerField(choices=SITUAÇAO, default=False)
    criseEspaçoInterior = models.IntegerField(choices=SITUAÇAO, default=False)
    exposiçãoRisco = models.IntegerField(choices=SITUAÇAO, default=False)
    qualidadeSono = models.IntegerField(choices=SITUAÇAO, default=False)
    tentativaSuicidio = models.IntegerField(choices=SITUAÇAO, default=False)
    qualidadeEscuta = models.IntegerField(choices=SITUAÇAO, default=False)
    maturidadeEmocional = models.IntegerField(choices=SITUAÇAO, default=False)
    qualidadeNutritiva = models.IntegerField(choices=SITUAÇAO, default=False)
    autoMedicacao = models.IntegerField(choices=SITUAÇAO, default=False)
    intoleranciaFrustração = models.IntegerField(choices=SITUAÇAO, default=False)
