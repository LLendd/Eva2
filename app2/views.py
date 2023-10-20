from django.shortcuts import render

# Create your views here.

def renderTemplates(request):
    return render(request, 'templatesApp/app2.html')

def Juegos1(request):
    data={
        "informacion":"don't Starve es un videojuego de supervivencia con elementos de survival horror.",
        "fecha":"lanzado en 2013",
        "descargas":"100 millones +",

    }
    return render(request, 'templatesApp/juego1.html',data)


def Juegos2(request):
    data={
        "informacion":"A Hat in Time es un juego de plataforma ",
        'fecha':" octubre de 2017",
        'descargas':"100k +",
    }
    return render(request,'templatesApp/productos2.html',data)

def Juegos3(request):
    data={
        "informacion":"Fallout 4 es un juego de supervivenvia posapocaliptico",
        'fecha':"3 de junio de 2015",
        'descargas':"100k +",
    }
    return render(request,'templatesApp/productos2.html',data)


