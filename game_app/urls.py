
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_app.commons.urls')),
    path('game/', include('game_app.games.urls')),
    path('profile/', include('game_app.accounts.urls')),

]
