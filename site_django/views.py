from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def catalog(request):
    products = ["Кільця", "Сережки", "Браслети", "Підвіски"]
    return render(request, 'catalog.html', {"products": products})

def contacts(request):
    return render(request, 'contacts.html')