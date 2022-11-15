from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request ,'index.html')
    # return HttpResponse('Home')

def about(request):
    return render(request ,'about.html')
    # return HttpResponse('About Us')
def contact(request):
    return render(request ,'contact.html')
    #return HttpResponse('contact')