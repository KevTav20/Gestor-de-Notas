from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, User

@login_required
def index(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    notes = user.notes.all()  # Obtener todas las notas del usuario
    context = {'user': user, 'notes': notes}
    return render(request, "notes_TaveraMujica/list.html", context)  # Template 'list.html'

@login_required
def detail(request, user_id, note_id):
    user = get_object_or_404(User, pk=user_id)
    note = get_object_or_404(Note, pk=note_id, user=user)
    context = {'user': user, 'note': note}
    return render(request, "notes_TaveraMujica/detail.html", context)  # Template 'detail.html'

@login_required
def create(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(user=user, title=title, content=content)
        return redirect('notes_TaveraMujica:index', user_id=user.id)
    return render(request, "notes_TaveraMujica/create.html", {'user': user})  # Template 'create.html'

@login_required
def edit(request, user_id, note_id):
    user = get_object_or_404(User, pk=user_id)
    note = get_object_or_404(Note, pk=note_id, user=user)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notes_TaveraMujica:detail', user_id=user.id, note_id=note.id)
    return render(request, "notes_TaveraMujica/edit.html", {'user': user, 'note': note})  # Template 'edit.html'

@login_required
def delete(request, user_id, note_id):
    user = get_object_or_404(User, pk=user_id)
    note = get_object_or_404(Note, pk=note_id, user=user)
    if request.method == "POST":
        note.delete()
        return redirect('notes_TaveraMujica:index', user_id=user.id)
    return render(request, "notes_TaveraMujica/delete.html", {'user': user, 'note': note})  # Template 'delete.html'
