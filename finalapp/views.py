from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import *
from .models import Qradar


# project all the data into webpage

@login_required
def alldata(request):
    obj = Qradar.objects.all()
    return render(request, 'finalapp/home.html', {'obj1': obj})


@login_required
def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Qradar.objects.filter(Q(log_source__icontains=srch))

            if match:
                return render(request, 'finalapp/search.html', {'sr': match})
            else:
                messages.error(request, f'Invalid Input')

        else:
            return HttpResponseRedirect('/search')

    return render(request, 'finalapp/search.html')
