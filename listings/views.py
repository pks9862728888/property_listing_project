from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,
                                  ListView)
from django.core.paginator import Paginator
from .models import Listing
from .choices import (state_choices,
                      bedroom_choices,
                      price_choices)

class IndexView(ListView):
    model = Listing
    context_object_name = 'listings'
    template_name = 'listings/listings.html'
    paginate_by = 3
    queryset = Listing.objects.all().filter(
        is_published=True).order_by('-list_date')


def listingView(request, pk):
  listing = get_object_or_404(Listing, pk=pk)
  return render(request, 'listings/listing.html', context={'listing' : listing})
  

def searchView(request):
    search_results = Listing.objects.all().order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            search_results = search_results.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            search_results = search_results.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            search_results = search_results.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            search_results = search_results.filter(bedrooms__lte=bedrooms)
    
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            search_results = search_results.filter(price__lte=price)

    # Pagination
    paginator = Paginator(search_results, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # Context dict
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'search_results': paged_listings,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context=context)
