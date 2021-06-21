from django.shortcuts import render

# Create your views here.
from app.form import Loginform

def login_view(request):
    form = Loginform()

    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['UserName'])
            print(form.cleaned_data['PassWord'])
            
    context = {
        'form':form
    }
    
    return render(request, 'login.html', context)
