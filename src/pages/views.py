from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from .models import Note, Log

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
	if n.user_id==request.user.id:
		n.delete()
		#logAction(n.user_id, str(n.user_id) + " deleted '" + n.text + "'")
	return redirect('/')

@login_required
def addNoteView(request):
	text = request.POST.get('note')
	id = request.user.id
	query = "INSERT INTO pages_note (user_id, text) VALUES (" + str(id) + ",'" + text + "')"
	print(query)
	connection.cursor().execute(query)
	#logAction(id, str(id) + " added '" + text + "'")
	return redirect('/')
	#	text = request.POST.get('note')
	#	n = Note(user_id=request.user.id, text=text)
	#	n.save()
	#logAction(id, str(id) + " added '" + text + "'")
	#	return redirect('/')

@login_required
def homePageView(request):
	notes = Note.objects.filter(user_id=request.user.id)
	return render(request, 'pages/index.html', {'notes': notes})

@login_required
def logView(request):
	#if request.user.is_superuser:
	#	logs = Log.objects.all()
	#	return render(request, 'pages/logs.html', {'logs': logs})
	#else:
	#	return redirect('/')
	logs = Log.objects.all()
	return render(request, 'pages/logs.html', {'logs': logs})

def logAction(id, action):
	log = Log(user_id=id, action=action)
	log.save()