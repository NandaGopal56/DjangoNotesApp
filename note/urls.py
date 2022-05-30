from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.getNotes, name='get-all-notes'),
    path('note/<pk>', views.getNote, name='get-single-notes'),
    path('note/create/', views.createNote, name='create-anotes'),
    path('note/<pk>/update/', views.updateNote, name='update-a-notes'),
    path('note/<pk>/delete/', views.deletenote, name='delete-a-notes'),

    # RESTFULL ROUTES
    path('notesapp/<pk>/', views.notesapp, name='GET-PUT-DELETE-a-note')
]