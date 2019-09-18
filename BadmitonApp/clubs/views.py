from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from clubs.models import Session, Player, Match, Club


#Create your views here.

# def club(request, club_id):
#    try:
#        club = Club.objects.get(id=id)
#    except Club.DoesNotExist:
#        raise Http404("Match does not exist")
#    return HttpResponse ("This is {} club page".format(club.name))


def index(request):
    club_list = Club.objects.order_by('name')[::]
    context = {
        'club_list':club_list,
     }

    return render (request, 'clubs/index.html',context)

def session_list(request, club_id):
    session_list = Session.objects.filter(club=club_id)
    # session_names = [s.session_name for s in session_list] # ['wednesday', 'tuesday']
    # session_start = [s.starting_time for s in session_list]
    context = {
        'session_list':session_list,
        # 'session_start':starting_time',
    }

    return render(request, 'clubs/session.html', context)
    # return HttpResponse(', '.join(session_names))

def session (request,id):
    try:
        session = Session.objects.get(id=id)
        context = {
            'session_text':session_name,
            'starting_time':starting_time,
         }
    except Club.DoesNotExist:
         raise Http404("Question does not exist")
    return render(request, 'clubs/detail.html',context)


#def player(request,id):
#    player = Player.objects.get(id=id)

#    return HttpResponse("Player session {} name {}".format(id, player.name))

#def match(request, id):
#    try:
#        match = Match.objects.get(id=id)
#    except Match.DoesNotExist:
#        raise Http404("Question does not exist")
#    return HttpResponse ("Match page")
