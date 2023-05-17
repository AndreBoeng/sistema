# Generated by Django 4.2 on 2023-05-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cad_Clientes', '0004_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_clientes',
            name='bairro',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='cep',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='cidade',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='complemento',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='estado',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='numero_casa',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='rua',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='cad_clientes',
            name='telefone2',
            field=models.IntegerField(blank=True),
        ),
    ]