from django.urls import path

from .views import homePageView, createUserView, deleteNoteView, addNoteView, logView, loginView

urlpatterns = [
    path('', homePageView, name='home'),
    path('createUser/', createUserView, name='createUser'),
    path('addNote/', addNoteView, name='addNote'),
    path('deleteNote/', deleteNoteView, name='deleteNote'),
    path('logs/', logView, name='logs'),
    path('login/', loginView, name='login'),
]
