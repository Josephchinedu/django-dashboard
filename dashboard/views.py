from django.shortcuts import render
from .models import *

# Create your views here.
def dash_board(request):
    context = {
        "project": Project.objects.all()[:6],
        "recent_work": Project.objects.all()[::-1][:4] # last 4 recent project
    }
    return render(request, 'index.html', context)
