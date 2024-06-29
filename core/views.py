from django.shortcuts import render
from django.http import HttpResponse
from core.models import Timecard


# Create your views here.
def index(request):

    rows = Timecard.objects.all()

    context = {
        'rows': rows
    }
    return render(request,"index.html", context)
