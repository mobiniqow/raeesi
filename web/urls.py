from django.urls import path
from web.views import *

app_name = 'web'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
    path('search', SearchView.as_view(), name='search'),
    path('category', CategoryView.as_view(), name='category'),
    path('show-news/<int:id>', ShowNewsView.as_view(), name='show-news'),
]
