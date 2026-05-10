from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from studies.models import Materia

# Create your views here.

def home_view(request):
    context = {}

    if request.user.is_authenticated:
        materias = Materia.objects.filter(user=request.user)
        context={
            "materias": materias
        }

    return render(
        request=request,
        template_name='core/home.html',
        context=context

    )
