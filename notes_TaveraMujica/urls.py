from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "notes_TaveraMujica"

urlpatterns = [
    # Página de login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(next_page='notes_TaveraMujica:login'), name='logout'),
    # Notas (solo accesibles después del login)
    path('<int:user_id>/', views.index, name="index"),
    path("<int:user_id>/<int:note_id>/detail/", views.detail, name="detail"),
    path("<int:user_id>/create/", views.create, name="create"),
    path("<int:user_id>/<int:note_id>/edit/", views.edit, name="edit"),
    path("<int:user_id>/<int:note_id>/delete/", views.delete, name="delete"),
]
