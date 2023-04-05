from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

# Create your views here.
def account(request):
    return render(request, 'account.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form not valid'
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form,'msg':msg})