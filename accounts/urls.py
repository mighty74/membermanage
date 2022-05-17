from django.urls import path
from . import views

#appの名前
app_name ='accounts'

#それぞれのurl先を指定
urlpatterns =[
    path('', views.Login.as_view(), name='start'),
    path('login/', views.Login.as_view(), name='login'),
    path('accountCreate/', views.Create_account.as_view(), name='accountcreate'),
    path('logout/', views.Logout.as_view(), name='logout'),
]