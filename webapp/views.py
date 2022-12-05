from django.shortcuts import render, HttpResponse
from.models import BlogPost

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

def blogHome(request):
    allPosts = BlogPost.objects.all
    context = {'allPosts':allPosts}
    return render(request, 'blogHome.html', context)

def blogPost(request, slug):
    q = BlogPost.objects.filter(slug__iexact = slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {
    'post': q
    }
    return render(request, 'blogPost.html', context)