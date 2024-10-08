from django.urls import path

from .views import homePageView, createUserView

urlpatterns = [
    path('', homePageView, name='home'),
    path('createUser/', createUserView, name='createUser')
]
