from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path("contact", views.contact, name='contact'),
    path('register', views.registerPage, name='register'),
    path('blog', views.blog, name='blog'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
]
