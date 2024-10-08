from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Note

def createUserView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login/')
	else:
		form = UserCreationForm()
	return render(request, 'pages/createUser.html', { "form" : form})

@login_required
def deleteNoteView(request):
	n = Note.objects.get(pk=request.POST.get('id'))
	if n.owner==request.user:
		n.delete()
	return redirect('/')

@login_required
def addNoteView(request):
	text = request.POST.get('note')
	n = Note(owner=request.user, text=text)
	n.save()
	return redirect('/')

@login_required
def homePageView(request):
	notes = Note.objects.filter(owner=request.user)
	#uploads = [{'id': n.id, 'text': n.text} for n in notes]	
	return render(request, 'pages/index.html', {'notes': notes})
