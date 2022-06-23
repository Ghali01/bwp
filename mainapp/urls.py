from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('register',register,name='register'),
    path('library',library,name='library'),
    path('add-item',addItem,name='add-item'),
    path('update-item/<int:pk>',updateItem,name='update-item'),
    path('delete-item/<int:pk>',deleteItem,name='delete-item'),
    path('login-admin',loginV,name='login'),

]