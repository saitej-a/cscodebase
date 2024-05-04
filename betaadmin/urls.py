from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name='beta'),
    path('admin/', admindashboard, name='admin'),
    path('logout/',logout,name='logout'),
    path('login/',login,name='login'),
    path('signup/',register,name='signup'),
    path('editProfile/',editprofile,name='editprofile'),
    path('viewprofile/<str:id>/',viewProfile,name='viewprofile'),
    path('forget-password/',forget,name='forget')
]