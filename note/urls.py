from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notes/', views.getNotes),
    path('note/<pk>', views.getNote),
    path('note/create/', views.createNote),
    path('note/<pk>/update/', views.updateNote),
    path('note/<pk>/delete/', views.deletenote),

    # RESTFULL ROUTES
    path('notesapp', views.notesapp)
]