from django.shortcuts import render
from django.http import HttpResponse
from core.models import Timecard, Employee
from core.service.TimecardService import TimecardService


# Create your views here.
def index(request):

    context = {
        'rows': Timecard.objects.all()
    }

    return render(request,"index.html", context)


def get_timecard_by_emp_full_name(request):

    row = TimecardService.get_timecard_by_emp_full_name(request.GET['full_name'])

    context = {
        "rows": row,
        "full_name": request.GET['full_name']
    }

    return render(request,"index.html", context)