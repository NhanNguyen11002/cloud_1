from django.urls import path

from . import views

app_name = 'gameserver'
urlpatterns = [
    path('<int:tiles>', views.game_server),
]
