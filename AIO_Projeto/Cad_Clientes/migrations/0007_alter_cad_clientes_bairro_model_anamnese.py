# Generated by Django 4.2 on 2023-05-18 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cad_Clientes', '0006_alter_cad_clientes_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_clientes',
            name='bairro',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='Model_anamnese',
            fields=[
                ('id_anamnese', models.AutoField(primary_key=True, serialize=False)),
                ('anamnese', models.TextField(blank=True)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cad_Clientes.cad_clientes')),
            ],
        ),
    ]