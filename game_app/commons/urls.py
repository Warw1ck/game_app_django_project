from django.urls import path

from game_app.commons import views

urlpatterns =[
    path('', views.home_page, name='home'),
    path('dashboard', views.dashboard_page, name='dashboard games'),

]