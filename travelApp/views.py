from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from itineraries.models import *
from django.contrib.auth import authenticate
from .forms import *
from django.contrib.auth.models import User
from django.views import generic

class auth_user(generic.FormView):
    form_class = AuthUser
    template = "auth_user.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect("/")
        else:
            form = AuthUser

        return render(request, self.template,
            {
                "form" : form,
            })

def all_itineraries(request):
    itineraries = Itinerary.objects.order_by('-id')[:5]
    output = ', '.join([q.get_name() for q in itineraries])
    return HttpResponse(output)

def index(request):
    return HttpResponse("Hello World!", request)