from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name="home"),
    path('',views.dashboard,name="dashboard"),
    path('add_online_member',views.add_online_member,name="add_online_member"),

]