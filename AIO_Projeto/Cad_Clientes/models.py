from django.db import models

# Create your models here.
class Cad_Clientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False)
    cpf = models.IntegerField(blank=False)
    data_nascimento = models.IntegerField(blank=False)
    sexo = models.CharField(max_length=3,blank=False)
    rua = models.CharField(max_length=50,blank=True)
    numero_casa = models.IntegerField(blank=True)
    complemento = models.CharField(max_length=50,blank=True)
    bairro = models.CharField(max_length=50,blank=True)
    cidade = models.CharField(max_length=50,blank=True)
    estado = models.CharField(max_length=2,blank=True)
    cep = models.IntegerField(blank=True)
    email = models.EmailField(max_length=50,blank=True)
    telefone = models.IntegerField(blank=False)
    telefone2 = models.IntegerField(blank=True)
