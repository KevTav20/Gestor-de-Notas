from django.urls import path

from project_TaveraMujica.urls import urlpatterns
from . import views
from django.urls import path

app_name = "notes_TaveraMujica"

urlpatterns = [
    #/notes_TaveraMujica/
    path("", views.index, name = "index"),
    #
    path("<int:user_id>/<int:note_id>/", views.list, name = "list"),
    path("<int:user_id>/<int:note_id>/detail", views.detail, name = "detail"),
    path("<int:user_id>/create", views.create, name = "create"),
    path("<int:user_id>/delete", views.delete, name = "delete"),
    path("<int:user_id>/edit", views.edit, name = "edit"),

]