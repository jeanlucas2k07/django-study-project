from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Materia, SessaoEstudo
from django.contrib import messages
from datetime import time, timedelta

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

    materia = get_object_or_404(
        Materia,
        id=materia_id,
        user=request.user
    )

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        cor = request.POST.get('cor')

        if not all([cor.strip(), descricao.strip(), nome.strip()]):
            messages.error(
                request=request,
                message='Preencha todos os campos'
            )
    
            return redirect(
                'studies:editar_materia',
                materia_id=materia_id
            )

        materia.nome = nome.strip()
        materia.descricao = descricao.strip()
        materia.cor = cor.strip()

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
    materia = get_object_or_404(Materia, id=materia_id, user=request.user)

    if request.method == 'POST':
        materia.delete()

    return redirect('core:home')


@login_required
def timer_sessao_view(request):
    return render(
        request=request, 
        template_name='studies/criar_sessao.html',
    )


@login_required
def finalizar_sessao_view(request):
    materias = Materia.objects.filter(user=request.user)
    context={
        "materias": materias
    }

    if request.method == 'POST':
        materia = request.POST.get('materia')
        observacoes = request.POST.get('observacoes')
        duracao = request.POST.get('duracao')

        if not all([materia, duracao.strip()]):
            messages.error(
                request=request,
                message='Materia ou duração estão vazios'
            )

            return redirect(
                to='studies:finalizar_sessao'
            )

        duracao = int(duracao)

        duracao_formatada = timedelta(seconds=duracao)
        print('Duração:', duracao_formatada)
        
        SessaoEstudo.objects.create(
            user=request.user,
            materia=Materia.objects.get(id=materia, user=request.user),
            duracao=duracao_formatada,
            observacoes=observacoes
        )

    return render(
        request=request, 
        template_name='studies/finalizar_sessao.html',
        context=context
    )