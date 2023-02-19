from django.urls import path,include
from website import views
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('career/', views.career, name='career'),
    path('products/', views.products, name='products'),
    path('module/<str:name>/', views.module, name='module'),
    
    
]