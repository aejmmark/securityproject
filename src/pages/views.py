from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def homePageView(request):
	return render(request, 'pages/index.html')

def createUserView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login/')
	else:
		form = UserCreationForm()
	return render(request, 'pages/createUser.html', { "form" : form})
