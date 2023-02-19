from django.contrib import admin
from django.urls import path, include
from itineraries.views import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sights/', include('sights.urls')),
    path('', index, name="index"),
    path('login/', auth_user.as_view(), name="auth_user"),
    path('all/', all_itineraries, name="all"),
    path('plan/create/', createItinerary, name="create_itinerary"),
    path('plan/<int:id>/', plan_redirect, name="plan_redirect"),
] 