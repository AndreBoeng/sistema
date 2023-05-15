from django.db import models

# Create your models here.
class Cad_Clientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.IntegerField()
    data_nascimento = models.IntegerField()
    sexo = models.CharField(max_length=3)
    rua = models.CharField(max_length=255)
    numero_casa = models.IntegerField()
    complemento = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.IntegerField()
    email = models.EmailField(max_length=254)
    telefone = models.IntegerField()
    telefone2 = models.IntegerField()
