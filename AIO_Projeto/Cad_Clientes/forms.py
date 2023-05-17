from django import forms
from .models import Cad_Clientes

#Eu tenho um Model/Banco de Dados único, que inserem quase todas as informações possíveis dos clientes.
#Entretanto, eu tenho forms, que me permitem identificar os formulários que eu desejo enviar para as views.
#O interessante é usar o menor possivel de banco de dados, criando menos bancos de dados e menos informações duplicadas.
#Criar o maximo de forms possiveis para manipular quais dados serão inseridos e manipulados.

sexo = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

estados = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

class form_cadastro_cliente(forms.ModelForm, forms.Form):
  
    class Meta:
        model = Cad_Clientes
        fields = "__all__"
        

    #Se eu quiser utilizar desta forma, terei de utilizar o metodo POST.GET,
    #Teria que coletar as informações pelo metodo POST, pela VIEW.
    
    # nome = forms.CharField(label="Nome", max_length=50, required=True)
    # cpf = forms.IntegerField(label="CPF", required=True)
    # data_nascimento = forms.IntegerField(label="Data_nascimento", required=True)
    # sexo = forms.MultipleChoiceField(required=True, label="Sexo", choices=sexo)
    # rua = forms.CharField(label="Rua", required=False )
    # numero_casa = forms.IntegerField(label="Numero da Casa",required=False)
    # complemento = forms.CharField(label="Complemento", required=False, max_length=50)
    # bairro = forms.CharField(label="Bairro", required=False)
    # cidade = forms.CharField(label="Cidade", required=False,max_length=50)
    # estado = forms.MultipleChoiceField(label="Estado", choices=estados, required=False)
    # cep = forms.IntegerField(label="CEP", required=False)
    # email = forms.EmailField(label="Email", required=False)
    # telefone = forms.IntegerField(label="Telefone", required=True)
    # telefone2 = forms.IntegerField(label="Telefone", required=False)

    
#     # def clean_confirma_senha(self):
#     #     confirma_senha = self.cleaned_data.get('confirma_senha')
#     #     senha = self.cleaned_data.get('senha')
#     #     if confirma_senha != senha:
#     #         raise forms.ValidationError('As senhas não conferem.')
#     #     return confirma_senha
    
#     def clean_senha(self):
#         senha = self.cleaned_data.get('senha')
#         if len(senha) < 8:
#             raise forms.ValidationError('A senha deve ter no mínimo 8 caracteres.')
#         return senha
#     def clean_confirma_senha(self):
#         confirma_senha = self.cleaned_data.get('confirma_senha')
#         senha = self.cleaned_data.get('senha')
#         if confirma_senha != senha:
#             raise forms.ValidationError('As senhas não conferem.')
#         return confirma_senha

    
    