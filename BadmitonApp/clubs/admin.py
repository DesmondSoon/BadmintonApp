from django.contrib import admin

from.models import Session
from.models import Player
from.models import Match
from.models import Club
# Register your models here.
admin.site.register(Session)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Club)
