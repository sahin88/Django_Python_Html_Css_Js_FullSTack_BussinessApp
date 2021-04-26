
from django.urls import path
from .  import  views
from roza.views import ProductListView 


urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('products', ProductListView.as_view(), name="product"),
    path('detail/<int:id>', views.application_detail, name="application_detail"),
    path('send_mail', views.send_email, name="send_mail"),
    path('thanks/', views.thanks, name="thanks"),
]
