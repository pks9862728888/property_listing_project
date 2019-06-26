from django.shortcuts import render
from django.views.generic import ListView
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import (state_choices,
                              bedroom_choices,
                              price_choices)

class IndexListView(ListView):
    model = Listing
    template_name = "pages/index.html"
    context_object_name = 'listings'
    
    def get_queryset(self):
        latest_listing = Listing.objects.all().filter(
            is_published=True).order_by('-list_date')[:3]
        queryset = {
            'latest_listing': latest_listing,
            'state_choices' : state_choices,
            'bedroom_choices' : bedroom_choices,
            'price_choices' : price_choices
        }
        return queryset

class AboutView(ListView):
    model = Realtor
    template_name = "pages/about.html"
    context_object_name = 'realtors'

    def get_queryset(self):
        queryset = {'all_realtors': Realtor.objects.all(), 
                    'mvp_realtor': Realtor.objects.all().filter(is_mvp=True)}
        return queryset
