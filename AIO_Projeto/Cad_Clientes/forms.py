from django import forms
from .models import Cad_Clientes

#Eu tenho um Model/Banco de Dados único, que inserem quase todas as informações possíveis dos clientes.
#Entretanto, eu tenho forms, que me permitem identificar os formulários que eu desejo enviar para as views.
#O interessante é usar o menor possivel de banco de dados, criando menos bancos de dados e menos informações duplicadas.
#Criar o maximo de forms possiveis para manipular quais dados serão inseridos e manipulados.

class form_cadastro_cliente(forms.ModelForm):

    class Meta:
        model = Cad_Clientes
       