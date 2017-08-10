import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

def main(request):
    return render(request, 'dashboard/main.html')
