from django.shortcuts import render
from products.models import Product, Offer


def home(request):
    offers = Offer.objects.filter(active=True).order_by('-id')[:6]
    loop_times = range(5)
    title = "Hola mundo"
    context = {'title': title, 'offers': offers, 'loop_times': loop_times}
    return render(request, "index.html", context)


def about(request):
    title = "About DMS"
    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do\
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\
        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip\
        ex ea commodo consequat. Duis aute irure dolor in reprehenderit in\
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur\
        sint occaecat cupidatat non proident, sunt in culpa qui officia \
        deserunt mollit anim id est laborum."
    context = {'title': title, 'text': text}
    return render(request, "about.html", context)


def services(request):
    title = "Services"
    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do\
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\
        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip\
        ex ea commodo consequat. Duis aute irure dolor in reprehenderit in\
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur\
        sint occaecat cupidatat non proident, sunt in culpa qui officia \
        deserunt mollit anim id est laborum."
    context = {'title': title, 'text': text}
    return render(request, "services.html", context)


def contact(request):
    title = "Contact"
    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do\
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\
        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip\
        ex ea commodo consequat. Duis aute irure dolor in reprehenderit in\
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur\
        sint occaecat cupidatat non proident, sunt in culpa qui officia \
        deserunt mollit anim id est laborum."
    context = {'title': title, 'text': text}
    return render(request, "contact.html", context)
