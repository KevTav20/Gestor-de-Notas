from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Note, User

def welcome(request):
    return render(request, 'notes/index.html')
def login(request):
    user = None  # Initialize user variable
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            # Busca el usuario por correo
            user = User.objects.get(email=email)
            # Verifica si la contraseña coincide
            if user.password == password:  # Asegúrate de manejar la contraseña de manera segura
                request.session['user_id'] = user.id  # Almacena el ID del usuario en la sesión
                return redirect('notes_TaveraMujica:list', user_id = user.id)
            else:
                messages.error(request, 'Correo o contraseña incorrectos')
        except User.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')

    context = {}  # Initialize context
    if user:  # Add user to context if available
        context['user'] = user
    return render(request, "notes/login.html", context)


def list_user(request):
    lista_usuarios = User.objects.all()
    context = {
        "lista_usuarios": lista_usuarios
    }
    return render(request, "notes/usuarios.html", context)


def detail(request, user_id, note_id):
    user = get_object_or_404(User, pk=user_id)
    note = get_object_or_404(Note, pk=note_id, user=user)
    context = {'user': user, 'note': note}
    return render(request, "notes/detail.html", context)

def list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    notes = user.notes.all()  # Obtener todas las notas del usuario
    context = {'user': user, 'notes': notes}
    return render(request, "notes/list.html", context)  # Template 'list.html'

def create(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(user = user, title=title, content=content)
        return redirect('notes_TaveraMujica:list', user_id=user.id)
    return render(request, "notes/create.html", {'user': user})  # Template 'create.html'


def edit(request, user_id, note_id):
    user = get_object_or_404(User, pk=user_id)
    note = get_object_or_404(Note, pk=note_id, user=user)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notes_TaveraMujica:detail', user_id=user.id, note_id=note.id)
    return render(request, "notes/edit.html", {'user': user, 'note': note})  # Template 'edit.html'


def delete(request, user_id, note_id):
    user = get_object_or_404(User, pk=user_id)
    note = get_object_or_404(Note, pk=note_id, user=user)
    if request.method == "POST":
        note.delete()
        return redirect('notes_TaveraMujica:list', user_id=user.id)
    return render(request, "notes/delete.html", {'user': user, 'note': note})  # Template 'delete.html'
