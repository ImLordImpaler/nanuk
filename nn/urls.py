from django.urls import path, include
from . import views
urlpatterns = [

    path('' , views.index , name='homepage'),
    path('reasons/' , views.reasons , name='reasons'),
    path('gallery/' , views.gallery , name='gallery'),


    path('login/' , views.loginPage , name='loginPage'),
    path('register/' , views.register , name='register'),
    path('logout/' , views.logoutPage , name='logoutPage')
]
