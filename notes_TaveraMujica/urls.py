from django.urls import path
from . import views

app_name = "notes_TaveraMujica"

urlpatterns = [
    # Página principal de bienvenida (pública)
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),  # Added trailing slash
    path('users/', views.list_user, name='users'),
    path('<int:user_id>/list', views.list, name="list"),
    path("<int:user_id>/<int:note_id>/detail/", views.detail, name="detail"),
    path("<int:user_id>/create/", views.create, name="create"),
    path("<int:user_id>/<int:note_id>/edit/", views.edit, name="edit"),
    path("<int:user_id>/<int:note_id>/delete/", views.delete, name="delete"),
]
