from django.shortcuts import render

# Create your views here.

def renderTemplates(request):
    return render(request, 'templatesApp/app2.html')
