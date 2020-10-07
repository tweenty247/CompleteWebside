from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact_page, name='contact'),
  path('about/', views.about, name='about'),
  path('services/', views.service, name='services'),
  path('pricing/', views.pricing, name='pricing'),
  path('blog', views.blog, name='blog'),
]

