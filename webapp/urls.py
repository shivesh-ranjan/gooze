from django.urls import path
from .views import *
urlpatterns = [
    # path('', views.index, name='index'),
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('blog/', blogHome),
    path('blog/blogPost/<str:slug>', blogPost, name="blogPost"),
]