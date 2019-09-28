from django.urls import path
from django.contrib import admin

from clubs.views import *


urlpatterns = [


    path('',index, name='index'),
    path('session/<id>',session, name = 'session'),
    path('<int:club_id>/', session_list, name='session list'),
    #path('<int:session_id>/player',views.player, name = 'player'),
    #path('match/<id>', views.match, name = 'match'),

    # localhost/clubs/5
    # -> clubs/<int:club_id>
    # -> clubs/<int:player_id>
    # -->player/1
]
