from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog_details/', blog_details, name='blog_details'),
    path('blog/', blog, name='blog'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('latest_news/', latest_news, name='latest_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('detail/', detail, name='detail')
]
