from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login' ),
    path('logout',views.logout,name='logout'),
    path('create',views.create,name='create'),
    path('read',views.read,name='read'),
    path('update',views.update,name='update'),
    path('update-record/<int:id>',views.update_record,name='update-record'),
    path('delete',views.delete,name='delete'),
    path('delete-record/<int:id>',views.delete_record,name='delete-record'),
    path('func',views.func,name='func'),
    path('forgot',views.forgot,name='forgot')
]
