from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from clubs.models import Session, Player, Match, Club

def home_view(request,):

    club_list = Club.objects.order_by('name')[::]
    context = {
        'club_list':club_list,
     }

    return render (request, 'home.html',context)
