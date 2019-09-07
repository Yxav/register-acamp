from django.shortcuts import render, redirect
from registro.forms import RegisterForm
from .models import Register

# Create your views here.
def home(request):
    return render(request, 'home.html')

def teste(request):
    return render (request, 'form.html')

def regs(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        form.is_valid()
        if form.is_valid():
            try:
                register = form.save()
                return redirect('inscription', register_id=register.id)
            except:
                pass
    else:
        form = RegisterForm()
    return render(request,'form.html',{'form':form})

def show(request, register_id):
    register = Register.objects.get(pk=register_id)
    registers = {'register':register}
    return render(request, 'show.html', registers)
