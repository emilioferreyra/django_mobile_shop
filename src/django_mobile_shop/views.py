from django.shortcuts import render


def home(request):
    title = "Hola mundo"
    context = {title: title}
    return render(request, "index.html", context)
