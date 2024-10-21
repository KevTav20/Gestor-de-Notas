from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
from .models import User, Note

def index(request):

    return render(request, "/notes/index.html", context)

def list(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    return render(request, "/notes/list.html", context)