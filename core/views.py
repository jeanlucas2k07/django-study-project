from django.shortcuts import render
from django.db.models import Sum
from studies.models import Materia, SessaoEstudo
from datetime import date, timedelta

# Create your views here.

def home_view(request):
    context = {}

    if request.user.is_authenticated:
        materias = Materia.objects.filter(user=request.user)
        sessoes = SessaoEstudo.objects.filter(user=request.user)
        today = date.today()

        total_materias = materias.count()
        total_sessoes = sessoes.count()

        tempo_total = sessoes.aggregate(
            total=Sum('duracao')
        )['total']
        dias_estudados = sessoes.values_list(
            'created_at__date',
            flat=True
        ).distinct()

        dias_estudados = set(dias_estudados)

        print(dias_estudados)

        sequencia = 0
        dia_verificado = today

        while dia_verificado in dias_estudados:
            sequencia += 1
            dia_verificado -= timedelta(days=1)
        
        print(sequencia)

        print(tempo_total)

        context={
            "materias": materias,
            "total_materias": total_materias,
            "total_sessoes": total_sessoes,
            "tempo_total": tempo_total,
            "sequencia": sequencia,

        }

    return render(
        request=request,
        template_name='core/home.html',
        context=context

    )
