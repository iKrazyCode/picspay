from django.shortcuts import render, HttpResponse
from .forms import CustomUserForm

# Create your views here.
def custom_login(request):
    context = {}

    context['form'] = CustomUserForm()
    return render(request, 'accounts/login.html', context=context)







