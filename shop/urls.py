from django.urls import path

from .views import HomePageView, AboutView, Contact_usCreateView

app_name = 'shop'
urlpatterns = [
    path('',HomePageView.as_view(),name='home-page'),
    path('about/', AboutView.as_view(),name='about-page'),
    path('contact/', Contact_usCreateView.as_view(),name='contact-page'),
]