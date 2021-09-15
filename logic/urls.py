from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contactUs/', views.contactForm, name='contactUsFormSubmit')
]