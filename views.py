from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
    

def success_view(request):
    return render(request, 'success.html')

def faq(request):
    return render(request, 'faq.html')

def case(request):
    return render(request, 'case.html')

def pricing(request):
    return render(request, 'pricing.html')

def team(request):
    return render(request, 'team.html')

