from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *

"""class createItinerary(generic.FormView):
    template = "itineraries/create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, 
            {
                "form" : CreateItinerary(request.POST, request.FILES),
            })
    
    def post(self, request, *args, **kwargs):
        form = CreateItinerary(request.POST)

        if form.is_valid():
            destination = form.cleaned_data.get("destination")
            start = form.cleaned_data.get("start")
            end = form.cleaned_data.get("end")

            new = Itinerary(destination=destination, start=start, end=end)
            new.save()

            return redirect("/sights/")

        else:
            form = CreateItinerary

        return render(request, self.template, 
            {
                "form" : form,
            })
"""


def createItinerary(request):
    if request.method == "POST":
        form = ItineraryForm(request.POST)

        if form.is_valid():
            form.save()

            itineraries = Itinerary.objects.order_by('-id')[:5]
            output = ', '.join([q.get_name() for q in itineraries])
            return HttpResponse(output)
            
        
    form = ItineraryForm
    return render(request, "itineraries/create.html", 
        {
            "form" : form
        })

def plan_redirect(request, id):
    return redirect("/plan/%s" % id, request)

class plan(generic.TemplateView):
    find_places_form_class = FindPlaces
    template = "itineraries\plan.html"

    def get(self, request, id, *args, **kwargs):
        object = get_object_or_404(Itinerary, pk=id)

        return render(request, self.template, 
            {
                "find_places_form" : self.find_places_form_class(),
                "object" : object,
                "trip_length" : object.get_trip_length(),
            })