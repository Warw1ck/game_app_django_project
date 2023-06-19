from django.urls import path

from game_app.accounts import views

urlpatterns =[
    path('create', views.profile_create, name='profile create'),
    path('details/<int:pk>', views.profile_details, name='profile details'),
    path('edit/<int:pk>', views.profile_edit, name='profile edit'),
    path('delete/<int:pk>', views.profile_delete, name='profile delete'),
]