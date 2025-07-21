from django.shortcuts import render


# Create your views here.
def homeView(request):
    template = 'home.html'
    context={
       
    }
    return  render(request, template, context)

def aboutView(request):
    template = 'about.html'
    context={
       
    }
    return  render(request, template, context)



def contactView(request):
    template = 'contact.html'
    context={
       
    }
    return  render(request, template, context)