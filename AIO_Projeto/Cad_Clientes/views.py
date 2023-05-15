from django.shortcuts import render, redirect
from .models import Cad_Clientes




# Create your views here.
def Cadastro_Clientes(request):
    return render(request, 'base/base_cad.html')


def listagem_clientes_request(request):

"""
#def listagem_clientes_request(request):
    novo_cliente = Cad_Clientes()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.id_paciente = request.POST.get('id_paciente')
    novo_cliente.cpf = request.POST.get('cpf')
    novo_cliente.data_nascimento = request.POST.get('data_nascimento')
    novo_cliente.sexo = request.POST.get('sexo')
    novo_cliente.rua = request.POST.get('rua')
    novo_cliente.numero_casa = request.POST.get('numero_casa')
    novo_cliente.complemento = request.POST.get('complemento')
    novo_cliente.bairro = request.POST.get('bairro')
    novo_cliente.cidade = request.POST.get('cidade')
    novo_cliente.estado = request.POST.get('estado')
    novo_cliente.cep = request.POST.get('cep')
    novo_cliente.email = request.POST.get('email')
    novo_cliente.telefone = request.POST.get('telefone')
    novo_cliente.telefone2 = request.POST.get('telefone2')
    novo_cliente.save()

   
    return render(request, 'central/cad_salvo.html')
    
"""
def Listagem_Clientes(request):
    listagem = {
        'clientes' : Cad_Clientes.objects.all()
        }
    return render(request, 'base/base_list.html', listagem)




#teste - curso 
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def post_create(request):

    form = PostForm()

    if(request.method == 'POST'):

        form = PostForm(request.POST)

        if(form.is_valid()):

            post_title = form.cleaned_data['title']
            post_slug = form.cleaned_data['slug']
            post_body = form.cleaned_data['body']
            post_author = form.cleaned_data['author']
            post_status = form.cleaned_data['status']

            new_post = Post(title=post_title, slug=post_slug, body=post_body, author=post_author, status=post_status)

            new_post.save()

            return redirect('D:\Programação\teste\AIO_Env\AIO_Projeto\Cad_Clientes\templates\Base\base_add_post.html')
        
    elif(request.method == 'GET'):
        
        return render(request, 'D:\Programação\teste\AIO_Env\AIO_Projeto\Cad_Clientes\templates\Base\base_add_post.html', {'form': form})"""