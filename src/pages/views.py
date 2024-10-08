from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
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
	if n.owner==request.user.id:
		n.delete()
	return redirect('/')

@login_required
def addNoteView(request):
	text = request.POST.get('note')
	id = request.user.id
	query = "INSERT INTO pages_note (owner, text) VALUES (" + str(id) + ",'" + text + "')"
	print(query)
	connection.cursor().execute(query)
	return redirect('/')

@login_required
def homePageView(request):
	notes = Note.objects.filter(owner=request.user.id)
	return render(request, 'pages/index.html', {'notes': notes})

#@login_required
#def deleteNoteView(request):
#	n = Note.objects.get(pk=request.POST.get('id'))
#	if n.owner==request.user:
#		n.delete()
#	return redirect('/')
#
#@login_required
#def addNoteView(request):
#	text = request.POST.get('note')
#	n = Note(owner=request.user.id, text=text)
#	n.save()
#	return redirect('/')
#
#@login_required
#def homePageView(request):
#	notes = Note.objects.filter(owner=request.user.id)
#	return render(request, 'pages/index.html', {'notes': notes})

#conn = sqlite3.connect(name)
#agents = read_database(conn)
#result = conn.execute("SELECT id, name FROM Agent ORDER BY id")
#agents = result.fetchall()