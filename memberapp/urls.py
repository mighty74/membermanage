from django.contrib import admin
from django.urls import path
from .views import Test, Home, Memberlist, About, CreateMember, DeleteMember, UpdateMember, CreateList, DeleteList


urlpatterns = [
    path('', Home.as_view(), name = 'start'),
    path('home/', Home.as_view(), name = 'home'),
    path('createlist/', CreateList, name = 'createlist'),
    path('deletelist/<int:id>/', DeleteList, name = 'deletelist'),
    path('memberlist/<int:id>/', Memberlist, name = 'memberlist'),
    path('create/<int:id>', CreateMember, name = 'create'),
    path('delete/<int:id>/', DeleteMember, name = 'delete'),
    path('about/<int:member_id>/', About, name = 'about'),
    path('update/<int:id>/', UpdateMember, name = 'update'),
    path('test/', Test.as_view(), name = 'test'),
]