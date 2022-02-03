from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def partner_apply(request):
    return render(request, 'partner_apply.html')

