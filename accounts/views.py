from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(
                request=request,
                message='As senhas não coincidem'
            )
        
            return redirect(
                to='auth:register'
            )
        
        if not username or not email or not password or not confirm_password:
            messages.error(
                request=request,
                message='Preencha todos os campos'
            )

            return redirect(
                to='auth:register'
            )
        
        if User.objects.filter(email=email).exists():
            messages.error(
                request=request,
                message='E-mail já cadastrado'
            )

            return redirect(
                to='auth:register'
            )
        
        if User.objects.filter(username=username).exists():
            messages.error(
                request=request,
                message=f'O username: {username} já está cadastrado'
            )

            return redirect(
                to='auth:register'
            )
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            login(
                request=request,
                user=user
            )

        except Exception as e:
            messages.error(
                request=request,
                message=f'Falha ao criar usuário: {e}'
            )

            return redirect(
                to='auth:register'
            )
        
        messages.success(
            request,
            'Conta criada com sucesso!'
        )
        
        return redirect(
            to='core:home'
        )
    
    return render(
        request=request,
        template_name='accounts/register.html'
    )

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(
                request=request,
                message='Preencha os campos'
            )

            return redirect('accounts:login')

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(
                request=request,
                user=user
            )

            return redirect(
                to='core:home'
            )
        else:
            messages.error(
                request=request,
                message='Username ou senhas incorretos'
            )

            return redirect('accounts:login')
    
    return render(
        request=request,
        template_name='accounts/login.html'
    )