from django.shortcuts import render

def homePageView(request):
	return render(request, 'pages/index.html')
