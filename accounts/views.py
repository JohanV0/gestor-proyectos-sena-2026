from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def registro(requets):
    datos = ''
    errors = []

    if requets.method == 'POST':
        username = requets.POST.get('username')
        email = requets.POST.get('email')
        first_name = requets.POST.get('first_name')
        last_name = requets.POST.get('last_name')
        password1 = requets.POST.get('password1')
        password2 = requets.POST.get('password2')

        datos = requets.POST

        #validacion basica 
        if password1 != password2:
            errors.append('Las contraseñas no coincides')
        if User.objects.filter(username=username).exists():
            errors.append('El nombre de usuario ya existe')
        if User.objects.filter(email=email).exists():
            errors.append('El correo electronico ya esta registrado')

        if not errors:
            #create_user hashea la contraseña automaticamente 
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name = first_name,
                last_name=last_name,
            )
            login(requets,user)
            return redirect('home')

    return render(requets, 'registro.html', {'errors' : errors, 'datos' : datos})