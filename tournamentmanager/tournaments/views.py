from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tournament

# Create your views here.


class TournamentListView(ListView):
    model = Tournament
    paginate_by = 100
