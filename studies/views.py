from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Materia
from django.contrib import messages

# Create your views here.
@login_required
def cadastrar_materia_view(request):
    if request.method == 'POST':
        cor = request.POST.get('cor')
        descricao = request.POST.get('descricao')
        nome = request.POST.get('nome')

        if not cor or not descricao or not nome:
            messages.error(
                request=request,
                message='Preencha todos os campos'
            )
        
            return redirect(
                'studies:cadastrar_materia'
            )
        
        try:
            Materia.objects.create(
                user=request.user,
                nome=nome,
                descricao= descricao,
                cor=cor
            )

            return redirect('core:home')

        except Exception as e:
            ...
        
    
    return render(
            request=request,
            template_name='studies/cadastrar_materia.html'
        )

@login_required
def editar_materia_view(request, materia_id):
    materia = Materia.objects.get(id=materia_id, user=request.user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        cor = request.POST.get('cor')

        if not cor or not descricao or not nome:
            messages.error(
                request=request,
                message='Preencha todos os campos'
            )
    
            return redirect(
                'studies:editar_materia',
                materia_id=materia_id
            )

        materia.nome = nome
        materia.descricao = descricao
        materia.cor = cor

        materia.save()

        return redirect('core:home')
    
    return render(
        request=request,
        template_name='studies/editar_materia.html',
        context={
            'materia': materia
        }
    )

@login_required
def deleter_materia_view(request, materia_id):
    materia = Materia.objects.filter(id=materia_id)

    if request.method == 'POST':
        materia.delete()

    return redirect('core:home')

@login_required
def criar_sessao_view(request):
    materias = Materia.objects.filter(user=request.user)
    context={
        "materias": materias
    }
    return render(
        request=request, 
        template_name='studies/criar_sessao.html',
        context=context
    )