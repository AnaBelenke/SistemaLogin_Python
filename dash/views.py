from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')  # Substitua 'home' pela sua URL de redirecionamento
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

