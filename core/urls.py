from django.contrib import admin
from django.urls import path

import core.views
from core import views as core

urlpatterns = [
    path('', core.index, name='core'),
    path('filterByFullName/', core.get_timecard_by_emp_full_name, name='core')
]