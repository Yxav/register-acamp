from django.shortcuts import render, redirect
from registro.forms import RegisterForm
from .models import Register

# Create your views here.
def home(request):
    return render(request, 'home.html')

def regs(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/inscricao')
            except:
                pass
    else:
        form = RegisterForm()
    return render(request,'form.html',{'form':form})

def show(request):
    register = Register.objects.last()
    registers = {'register':register}
    return render(request, 'show.html', registers)

def clean(request):
    register = 0
    registers = {'register':register}
