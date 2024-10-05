from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserForm


# Create your views here.
def custom_login(request):
    context = {}

    if request.user.is_authenticated == True:
        # redirect se estiver logado
        return redirect(reverse('home:home'))

    if request.method == 'POST':
        # Realizar o login
        form = CustomUserForm(data=request.POST)

        print(form.errors)
 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            else:
                print('credenciais incorretas.')
        else:
            print('Preencha o formulário corretamente')
            return redirect(reverse('accounts:login'))

        return redirect(reverse('accounts:login'))

    else:
        form = CustomUserForm()
        context['form'] = form
        return render(request, 'accounts/login.html', context=context)



def custom_register(request):
    if request.user.is_authenticated == True:
        return redirect(reverse('home:home'))
    
    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = get_user_model()
            try:
                user.objects.get(username=username)
                # Não pode criar, pois já existe
                print('Usuário já existe')

            except (user.DoesNotExist):
                user_create = user.objects.create(username=username, password=password)
                user_create.save()
                login(request, user_create)
                return redirect(reverse('home:home'))
            
        else:
            print('Preencha o formulário corretamente')

        return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html')




@login_required
def custom_logout(request):
    logout(request)
    return redirect(reverse('accounts:login'))


