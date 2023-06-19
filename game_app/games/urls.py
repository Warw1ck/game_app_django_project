from django.urls import path

from game_app.games import views


urlpatterns = [
    path('create', views.game_create, name='game create'),
    path('details/<int:pk>', views.game_details, name='game details'),
    path('edit/<int:pk>', views.game_edit, name='game edit'),
    path('delete/<int:pk>', views.game_delete, name='game delete'),

]