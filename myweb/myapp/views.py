from django.shortcuts import render
from django.http import HttpResponse
from .models import feature


# Create your views here.
def index(request):
    feature1 = feature()
    feature1.id = 0
    feature1.name = 'Farm fresh quality'
    feature1.details = "Direct from local farms to your table, ensuring maximum freshness and quality."

    feature2= feature()
    feature2.id = 1
    feature2.name = 'Flexible Delivery'
    feature2.details = "Choose delivery or pickup options that fit your schedule and preferences."
    feature3 = feature()
    feature3.id = 2
    feature3.name = 'Support Local'
    feature3.details = "Your purchase directly supports local farmers and sustainable agriculture."

    feature4 = feature()
    feature4.id = 3
    feature4.name = 'Transparent Sourcing'
    feature4.details = "Detailed information about farming practices, certifications, and origin."

    features = [feature1,feature2,feature3,feature4]

    return render(request, 'index.html',{'features': features })


